import unittest
from typing import Optional, List
from helpers import *

class _():
    '''
    34: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
    Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
    If target is not found in the array, return [-1, -1].
    You must write an algorithm with O(log n) runtime complexity.
    '''
    def sol1(self, nums: List[int], target: int) -> int:
        l = 0        
        L = len(nums)
        r = L - 1
        if L == 1 and nums[0]==target: return[0,0]
        while l<=r:
            m = (l+r)//2
            if nums[m]==target:
                l = m
                r = m
                while (l-1)>=0 and nums[l-1]==target: 
                    l-=1
                while (r+1)<L and nums[r+1]==target: 
                    r+=1
                return [l,r]
            else:
                if nums[m]<target: 
                    l = m+1
                else: 
                    r = m-1
        return [-1,-1]
    
class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        self.assertEqual(self.sol1(nums = [5,7,7,8,8,10], target = 8), [3,4])

if __name__ == "__main__":
    unittest.main()