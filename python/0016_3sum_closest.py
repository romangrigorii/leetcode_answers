import unittest
from typing import Optional, List
from helpers import *

class _ (Helpers):
    '''
    16: https://leetcode.com/problems/3sum-closest/description/ 
    Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
    Return the sum of the three integers.
    You may assume that each input would have exactly one solution.
    '''
    def sol1(self, nums: List[int], target) -> List[List[int]]:
        nums.sort()
        L = len(nums)
        outc, outa = abs(sum(nums[:3]) - target), sum(nums[:3]) # out for comare and out actual
        for i in range(L):
            l = i+1
            r = L-1
            targetn = nums[i] - target
            while l<r:
                s = targetn + nums[l] + nums[r]
                valc = abs(s)
                if valc < outc:
                    outc = valc
                    outa = s + target
                if s < 0:
                    l+=1
                elif s > 0:
                    r-=1
                else: 
                    return outa
        return outa
    
class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        self.assertEqual(self.sol1(nums = [-1,2,1,-4], target = 1), 2)
        self.assertEqual(self.sol1(nums = [0,0,0], target = 1), 0)
        self.assertEqual(self.sol1(nums = [1,1,1,1], target = 0), 3)
        self.assertEqual(self.sol1(nums = [1,1,1,0], target = 100), 3)
        self.assertEqual(self.sol1(nums = [4,0,5,-5,3,3,0,-4,-5], target = -2), -2)
        self.assertEqual(self.sol1(nums = [-1000,-5,-5,-5,-5,-5,-5,-1,-1,-1], target = -14), -15)

if __name__ == "__main__":
    unittest.main()