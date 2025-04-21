import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    94: https://leetcode.com/problems/binary-tree-inorder-traversal/
    Given the root of a binary tree, return the inorder traversal of its nodes' values.    
    '''
    def sol1(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ret = self.sol1(root.left)
        if root.val: ret += [root.val] + self.sol1(root.right)
        return ret
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol(self.tree_convf([1,None,2,None,None,3])), [1,3,2])
            


if __name__ == "__main__":
    unittest.main()
