import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    111: https://leetcode.com/problems/minimum-depth-of-binary-tree/
    Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.
    '''
    def sol1(self, root: Optional[TreeNode]) -> bool:
        if not root or root.val == None: return 0
        lft = self.sol1(root.left)
        rgt = self.sol1(root.right)
        mi = min(lft, rgt)
        ma = max(lft, rgt)
        q = mi if mi >0 else ma
        return 1 + q
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            s = self.tree_convf([3,9,20,None,None,15,7])
            s.print_tree_stack()
            self.assertEqual(sol(s), 2)


if __name__ == "__main__":
    unittest.main()
