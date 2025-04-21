import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    106: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
    Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary
    tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.
    '''
    def sol1(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder or not inorder:
            return None
        root=TreeNode(postorder[-1])
        index=inorder.index(postorder[-1])
        root.left=self.sol1(inorder[:index], postorder[:index])
        root.right=self.sol1(inorder[index+1:], postorder[index:-1])
        return root
    
    def sol2(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorderMap = { num:idx for idx,num in enumerate(inorder)}
        def helper(l, r):
            if l > r:
                return
            node = TreeNode(postorder.pop())
            idx = inorderMap[node.val]
            node.right = helper(idx+1,r)
            node.left = helper(l,idx-1)
            return node
        return helper(0,len(inorder)-1)
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1, self.sol2]:
            s = sol(inorder=[9,3,15,20,7], postorder = [9,15,7,20,3])
            s.print_tree_stack()
            self.assertEqual(self.tree_convb(s), [3,9,20,None,None,15,7])  

if __name__ == "__main__":
    unittest.main()
