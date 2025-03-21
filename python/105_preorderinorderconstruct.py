import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    105: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
    Given two integer arrays preorder and inorder where preorder is the preorder traversal of a 
    binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
    '''
    def sol1(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        Go through pre order items and check in the in order list if a value comes before or after a given element
        * This is my solution but doesn't pass LC because of time
        '''
        if len(preorder)>0 and len(inorder)>0:
            idx = inorder.index(preorder[0])
            i_left_list = inorder[:idx]
            i_right_list = inorder[idx+1:]            
            while idx>=len(preorder) or not all([q in i_left_list for q in preorder[1:idx+1]]):
                idx -=1
            p_left_list = preorder[1:idx+1]
            p_right_list = preorder[idx+1:]
            root = TreeNode(preorder[0], self.sol1(p_left_list, i_left_list), self.sol1(p_right_list, i_right_list))
            return root
        
    def sol2(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root=TreeNode(preorder[0])
        index=inorder.index(preorder[0])
        root.left=self.sol2(preorder[1:index+1],inorder[:index])
        root.right=self.sol2(preorder[index+1:],inorder[index+1:])
        return root

    def sol3(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        val_to_index = {val: i for i,val in enumerate(inorder)}
        def build(preorder, l, r):
            nonlocal val_to_index
            if not preorder or l > r:
                return None
            val = preorder.pop(0)
            root = TreeNode(val)
            root.left = build(preorder, l, val_to_index[val] - 1)
            root.right = build(preorder, val_to_index[val] + 1, r)
            return root
        return build(preorder, 0, len(inorder) - 1)
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1, self.sol2, self.sol3]:
            s = Tree(sol(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]))
            s.print_tree_stack()
            self.assertEqual(self.tree_convb(sol(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])), [3,9,20,None,None,15,7])
            


if __name__ == "__main__":
    unittest.main()
