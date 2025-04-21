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
        out = []
        def helper(root, cur, targetSum):
            if not root or root.val == None: return
            if not root.left and not root.right and root.val == targetSum: 
                out.append(cur + [root.val])
                return
            helper(root.left, cur + [root.val], targetSum - root.val)
            helper(root.right, cur + [root.val], targetSum - root.val)
        helper(root, [], targetSum)
        return out
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.hasPathSum]:
            s = self.tree_convf([5,4,8,11,None,13,4,7,2,None,None,None,None,1])
            s.print_tree_stack()
            self.assertEqual(sol(s, 22), [[5,4,11,2],[5,8,4,5]])


if __name__ == "__main__":
    unittest.main()
