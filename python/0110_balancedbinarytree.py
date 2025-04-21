import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    110: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
    Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.
    '''
    def sol1(self, root: Optional[TreeNode]) -> bool:
        self.bal = True
        def ln(node):
            if not node: return 0
            left_len = ln(node.left)
            right_len = ln(node.right)
            if abs(left_len - right_len)>1: 
                self.bal = False
            return 1 + max(left_len, right_len)
        ln(root)
        return self.bal
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol(self.tree_convf([3,9,20,None,None,15,7])), True)
            s = self.tree_convf([1,2,2,3,None,None,3,4,None,None,4])
            s.print_tree_stack()            
            self.assertEqual(sol(s), False)


if __name__ == "__main__":
    unittest.main()
