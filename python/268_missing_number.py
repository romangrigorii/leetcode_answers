import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    268: https://leetcode.com/problems/missing-number/
    Given an array of nums with n distinct numbers in range 0 n find the only missing number
    '''
    def sol1(self, nums: List[int]) -> int:
        '''
        This is my binary search solution. I think's it's the best approach.
        '''
        l = 0
        L = len(nums)
        r = L - 1
        nums.sort()
        if L == 1:
            if 0 == nums[0]: return 1
            else: return 0
        while r>l:
            m = int((l+r)/2)
            if r == nums[r]:
                return r+1
            if nums[l]>l:
                return l
            if m == nums[m]:
                l = m+1
            else:
                r = m
        return r

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol([9,6,4,2,3,5,7,0,1]), 8)
            self.assertEqual(sol([3,0,1]), 2)

if __name__ == "__main__":
    unittest.main()
