import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    108: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
    Given an integer array nums where the elements are sorted in ascending order, convert it to a 
    height-balanced binary search tree.
    '''
    def sol1(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None
        def helper(l,r):
            if l<=r:
                m = (l+r)//2
                tree = TreeNode()
                tree.val = nums[m]
                tree.left = helper(l,m-1)
                tree.right = helper(m+1,r)
                return tree
        return helper(0,len(nums)-1)

    def sol2(self, nums: List[int]) -> Optional[TreeNode]:
        '''
        sol2 is somehow 50% faster...
        '''
        def helper(l, r):
            if l > r: return None
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = helper(l, mid - 1)
            root.right = helper(mid + 1, r)
            return root
        return helper(0, len(nums) - 1)
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1, self.sol2]:
            self.assertEqual(self.tree_convb(sol(nums = [-10,-3,0,5,9])), [0, -10, 5, None, -3, None, 9])
            self.assertEqual(self.tree_convb(sol(nums = [1,3])), [3,1])
            


if __name__ == "__main__":
    unittest.main()
