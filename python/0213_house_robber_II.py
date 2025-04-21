import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    213: https://leetcode.com/problems/house-robber-ii/description/
    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
    All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile,
    adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses
    were broken into on the same night.
    Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
    '''
        
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        money0 = [0] * (1 + len(nums))
        money1 = [0] * (1 + len(nums))
        L = len(nums) - 1         
        for i in range(L):
            money0[i+2] = max(money0[i+1], money0[i] + nums[i])
            money1[i+2] = max(money1[i+1], money1[i] + nums[i+1])

        return max(money0[-1], money1[-1])

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.rob]:
            self.assertEqual(sol([2,3,2]), 3)
            self.assertEqual(sol([1,2,3,1]), 4)

if __name__ == "__main__":
    unittest.main()
