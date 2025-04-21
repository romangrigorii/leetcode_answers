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
        if len(nums) <= 1: return True
        if nums[0] == 0: return False
        jumps = 0
        curpos = 0
        curmax = nums[0]
        n = len(nums)
        while curmax < (n-1):
            curmax_ = curmax
            for i in range(curpos, curmax+1):
                if curmax < nums[i]+i:
                    curmax = nums[i]+i
            if curmax_ == curmax: return False
            pos = curmax_
        return True

    def sol2(self, nums: List[int]) -> int:
        steps = 0
        for num in nums:
            if steps < 0:
                return False
            elif num > steps:
                steps = num
            steps -= 1
        return True

class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.sol1, self.sol2]:
            self.assertEqual(sol([2,3,1,1,4]), True)
            self.assertEqual(sol([2,3,0,1,4]), True)
            self.assertEqual(sol([1,3,2]), True)
            self.assertEqual(sol([0,3,1]), False)

if __name__ == "__main__":
    unittest.main()
