import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    33: https://leetcode.com/problems/search-in-rotated-sorted-array/ 
    Given a rotated sorted array, develop a O(log(n)) algorithm that will find the index of a target value
    '''
    def sol1(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while r>=l:
            m = int((l+r)/2)
            if nums[m] == target: return m
            if nums[r] == target: return r
            if nums[l] == target: return l
            if nums[m]>nums[l] and nums[m]>target and nums[l]<target: # if the left array is sorted, and target falls in between two ends, go there
                r = m-1
            else: # else we go to the right array
                l = l+1
        return -1
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):
        self.assertEqual(self.sol1(nums = [4,5,6,7,0,1,2], target = 0), 4)
        self.assertEqual(self.sol1(nums = [4,5,6,7,0,1,2], target = 3), -1)
        self.assertEqual(self.sol1(nums = [1], target = 0), -1)

if __name__ == "__main__":
    unittest.main()