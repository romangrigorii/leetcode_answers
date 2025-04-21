import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    153: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
    Given a sorted array that has been rotated at a random index, find the minimum.
    The array may contain duplicate values
    '''
    def sol1(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        mi = float('inf')
        while l<=r:
            m = (l+r)//2
            if nums[m]>nums[l]: # sorted condition
                mi = min(mi, nums[l])
                l = m+1
            elif nums[m]<nums[l] : # unsorted condition
                mi = min(mi, nums[m])
                r = m-1
            else:
                mi = min(mi, nums[m])
                l+=1
        return mi

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol([2,2,2,0,1]), 0)
            self.assertEqual(sol([1,3,5]), 1)

if __name__ == "__main__":
    unittest.main()
