import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    109: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
    Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.
    '''
    def sol1(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head: return None
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        def helper(l,r):
            if l<=r:
                m = (l+r)//2
                tree = TreeNode()
                tree.val = nums[m]
                tree.left = helper(l,m-1)
                tree.right = helper(m+1,r)
                return tree
        return helper(0,len(nums)-1)
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(self.tree_convb(sol(self.convf([-10,-3,0,5,9]))), [0, -10, 5, None, -3, None, 9])
            


if __name__ == "__main__":
    unittest.main()
