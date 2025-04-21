import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    198: https://leetcode.com/problems/house-robber/description/ 
    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
    the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it 
    will automatically contact the police if two adjacent houses were broken into on the same night.
    Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
    '''
        
    def rob(self, nums: List[int]) -> int:
        money = [0,0] + [0]*len(nums)
        for i in range(len(nums)):
            money[i+2] = max(money[i] + nums[i], money[i+1])
        return money[-1]

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.rob]:
            self.assertEqual(sol([1,2,3,1]), 4)
            self.assertEqual(sol([2,7,9,3,1]), 12)

if __name__ == "__main__":
    unittest.main()
