import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    100: https://leetcode.com/problems/same-tree/
    Given the roots of two binary trees p and q, write a function to check if they are the same or not.
    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
    '''
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def issame(p,q):            
            if not p and not q: return True
            if not p or not q: return False
            return  p.val == q.val and issame(p.left, q.left) and issame(p.right, q.right)
        return issame(p,q)

class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.isSameTree]:
            self.assertEqual(sol(self.tree_convf([[1,2,3]]),self.tree_convf([[1,2,3]])), True)


if __name__ == "__main__":
    unittest.main()
