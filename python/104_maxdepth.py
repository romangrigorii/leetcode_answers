import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    104: https://leetcode.com/problems/maximum-depth-of-binary-tree/
    Given the root of a binary tree, return its maximum depth.
    A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
    '''
    def sol1(self, root):
        if not root: return 0
        return 1 + max(self.sol1(root.left), self.sol1(root.right))

    
class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.sol1]:
            self.assertEqual(sol(self.tree_convf([3,9,20,None,None,15,7])), 3)

if __name__ == "__main__":
    unittest.main()
