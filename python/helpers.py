from math import *
from collections import deque, Counter, defaultdict
class TreeNode():
    def __init__(self, val = None, leftchild = None, rightchild = None):
        self.val = val
        self.left = leftchild
        self.right = rightchild

    def tree_width_left_(tree):
        if tree:
            return 1 + TreeNode.tree_width_left_(tree.left)
        else:
            return 0
        
    def tree_width_right_(tree):
        if tree:
            return 1 + TreeNode.tree_width_right_(tree.right)
        else:
            return 0
        
    def tree_width(self):
        return (TreeNode.tree_width_left_(self if isinstance(self, TreeNode) else self.root), TreeNode.tree_width_right_((self if isinstance(self, TreeNode) else self.root)))
    
    def size(self, treenode):
        '''
        Counts the number of elements in a tree
        '''
        if not treenode: return 0
        return 1 + self.size(treenode.left) + self.size(treenode.right)

    def depth(self, treenode):
        '''
        Finds the depth of the tree
        '''
        if not treenode: return 0
        return 1 + max(self.depth(treenode.left),self.depth(treenode.right))
    
    def print_tree_stack(self):
        L = self.depth(self if isinstance(self, TreeNode) else self.root)
        lst = [[' ']*(2**L + 1) for q in range(L)]
        TreeNode.print_tree_helper_(self if isinstance(self, TreeNode) else self.root, lst, 0, L, int(2**(L-1)))
        for q in lst:
            print(" ".join([str(i) for i in q]))

    def print_tree_helper_(tree, lst, depth, L, pos):
        if tree:
            lst[depth][pos] = tree.val
            TreeNode.print_tree_helper_(tree.left, lst, depth+1, L, pos-(2**(L-depth-2)))
            TreeNode.print_tree_helper_(tree.right, lst, depth+1, L, pos+(2**(L-depth-2)))

class Tree(TreeNode):
    def __init__(self, root = None):
        self.root = root

    def tree_convf(self, lst):
        def helper(pos):            
            if pos<=len(lst):
                if lst[pos-1]!=None: return TreeNode(lst[pos-1], helper(pos*2), helper(pos*2+1))
                return None
            else:
                return None
        return helper(1)
    
    def tree_convb(self, tree):
        lst = [None]*(2**self.depth(tree) - 1)
        def helper(tree, pos):    
            if tree: 
                lst[pos-1] = tree.val
                helper(tree.left, pos*2)
                helper(tree.right, pos*2 + 1)
        helper(tree, 1)
        while lst and lst[-1] == None: lst = lst[:-1]
        lst_remove = [] # removing extra Nones
        for i in range(len(lst)):
            if lst[(i-1)//2] == None: lst_remove.append(i)
        lst = [lst[i] for i in range(len(lst)) if i not in lst_remove]
        return lst
    

class BST(Tree):
    def __init__(self, root = None):
        super().__init__(root)

    # Time:  0(N) operations where N is the size of the tree
    # Space: 0(log(n)) because we are at most keeping a stack of of log(n) values long 
        
    def find_maximum(self):
        return Tree.find_maximum_(self.root)
    
    @staticmethod
    def find_maximum_(tree):
        if not tree: return 0
        return max(Tree.find_maximum_(tree.left), Tree.find_maximum_(tree.right)) + tree.val
    
    def bst_convf(self, lst):
        lst.sort()
        self.elements = lst
        self.root = BST.initialize_from_lst_(lst)
        return self.root
        
    @staticmethod
    def initialize_from_lst_(lst): # given a list of values, recursively construct a BST
        if len(lst) == 0:
            return None
        tree = TreeNode()
        m = len(lst)//2
        tree.val = lst[m]
        tree.left = BST.initialize_from_lst_(lst[:m])
        tree.right = BST.initialize_from_lst_(lst[m+1:])
        return tree
    
    @staticmethod
    def bst_convb(ListNode):
        if not ListNode: return []
        return BST.bst_convb(ListNode.left) + [ListNode.val] + BST.bst_convb(ListNode.right)
        
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    @staticmethod
    def convf(nums):
        q = ListNode()
        qp = q
        for n in nums:
            q.next = ListNode()
            q = q.next
            q.val = n
        return qp.next
    
    @staticmethod
    def convb(ListNode):
        q = []
        while ListNode:
            q.append(ListNode.val)
            ListNode = ListNode.next
        return q

    @staticmethod
    def headat(node, idx):
        while node and idx:
            node = node.next
            idx -= 1
        return node
    
class Helpers(ListNode, BST):
    def equal_lists(self, list1, list2): # marks two lists as equal if contain the same elements
        if len(list1)!=len(list2):
            return False        
        while list1 and list2:
            a = list2.pop()
            if a not in list1: return False
            list1.remove(a)
        return not list1 and not list2

if __name__ == "__main__":
    helper = Helpers()
    bst = BST()
    tree = Tree()
    print(helper.equal_lists([1,2,3], [3,2,1]))
    print(helper.equal_lists([1,2,3], [3,2]))
    print(helper.equal_lists(helper.bst_convb(helper.bst_convf([1,5,8,4,3,5,1])), [1,1,3,4,5,5,8]))
    print(helper.tree_convb(helper.tree_convf([1,5,8,4,3,5,1])))
    print(helper.equal_lists(helper.tree_convb(helper.tree_convf([1,5,8,4,3,5,1]))[:7], [1,5,8,4,3,5,1]))
    print(helper.tree_convb(helper.tree_convf([3,9,20,None,None,15,7])))
    print(helper.equal_lists(helper.tree_convb(helper.tree_convf([3,9,20,None,None,15,7]))[:7], [3,9,20,None,None,15,7]))
