import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    75: https://leetcode.com/problems/sort-colors/description/
    Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, 
    with the colors in the order red, white, and blue.
    We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
    You must solve this problem without using the library's sort function.
    '''
    def sortColors(self, nums: List[int]) -> None:
        l,m,r = 0, 0, len(nums)-1
        while m!=r:
            if nums[m] == 2:
                nums[m], nums[r] = nums[r], nums[m]
                r-=1
            if nums[m] == 0:
                nums[m], nums[l] = nums[l], nums[m]
                l+=1
                m+=1
            if nums[m] == 1:
                m+=1
        return nums

class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.sortColors]:
            self.assertEqual(sol([2,0,2,1,1,0]),[0,0,1,1,2,2])

if __name__ == "__main__":
    unittest.main()
