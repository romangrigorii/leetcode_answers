import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    112: https://leetcode.com/problems/path-sum/
    Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path
    such that adding up all the values along the path equals targetSum. A leaf is a node with no children.
    '''
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        if not root.left and not root.right and root.val == targetSum: return True        
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.hasPathSum]:
            s = self.tree_convf([5,4,8,11,None,13,4,7,2,None,None,None,None,1])
            s.print_tree_stack()
            self.assertTrue(sol(s, 22))


if __name__ == "__main__":
    unittest.main()
