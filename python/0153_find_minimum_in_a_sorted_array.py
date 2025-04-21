import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    153: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array 
    Given a sorted array that has been rotated at a random index, find the minimum
    The array contains unique values
    '''
    def sol1(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        mi = float('inf')
        while r>=l:
            m = int((l+r+1)/2)
            if nums[m]>nums[l]: # if leftside is ordered
                if nums[l]<mi: # if left end is smaller than minimum thus far
                    mi = nums[l]
                l = m+1 # we shift attention to the other size
            else: # if they are not ordered on the left, we set the min to the middle because it's the min of the right (ordered) side. 
                if nums[m]<mi:
                    mi = nums[m]
                r = m-1         
        return mi

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol([3,4,5,1,2]), 1)
            self.assertEqual(sol([4,5,6,7,0,1,2]), 0)

if __name__ == "__main__":
    unittest.main()
