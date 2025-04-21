import unittest
from typing import Optional, List
from helpers import *
from collections import Counter

class _ :
    '''
    80: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
    There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
    Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such
    that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
    For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
    Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
    You must decrease the overall operation steps as much as possible
    '''
    def search(self, nums: List[int], target: int) -> bool:
        # Initilize two pointers
        l = 0
        r = len(nums) - 1 
        while l <= r:
            m = (l + r)//2
            if nums[m] == target:
                return True
            if nums[m] == nums[r]: # Fail to estimate which side is sorted
                r -= 1  # In worst case: O(n)
            elif nums[m] >= nums[l]: # Left side of m is sorted
                if  nums[l] <= target and target < nums[m]: # Target in the left side
                    r = m - 1
                else: # in right side
                    l = m + 1
            else: # Right side is sorted
                if  nums[m] < target and target <= nums[r]: # Target in the right side
                    l = m + 1
                else: # in left side
                    r = m - 1
        return False


class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.search]:
            self.assertEqual(sol([2,5,6,0,0,1,2], 0), True)
            self.assertEqual(sol([2,5,6,0,0,1,2], 3), False)

if __name__ == "__main__":
    unittest.main()
