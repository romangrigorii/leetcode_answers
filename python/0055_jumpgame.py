import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    55: https://leetcode.com/problems/jump-game/
    You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents 
    your maximum jump length at that position.
    Return true if you can reach the last index, or false otherwise.
    '''
    def sol1(self, nums: List[int]) -> int: # this solution takes too long
        out = [False]*len(nums)
        out[0] = True
        for i in range(len(nums)):
            if not out[i]: return False
            for k in range(1,nums[i]+1):
                if i+k>=len(nums): return True
                out[i+k] = True
        return out[-1]

    def sol2(self, nums: List[int]) -> int:
        steps = 0
        for num in nums:
            if steps < 0:
                return False
            elif num > steps:
                steps = num
            steps -= 1
        return True
    
    def sol3(self, nums: List[int]) -> bool:
        destination = len(nums) - 1
        for i in range(destination - 1, -1, -1):
            if( nums[i] + i >= destination):
                destination = i        
        return destination == 0

class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.sol1, self.sol2]:
            self.assertEqual(sol([2,3,1,1,4]), True)
            self.assertEqual(sol([2,3,0,1,4]), True)
            self.assertEqual(sol([1,3,2]), True)
            self.assertEqual(sol([0,3,1]), False)

if __name__ == "__main__":
    unittest.main()
