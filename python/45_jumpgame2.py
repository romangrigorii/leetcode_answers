import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    45: https://leetcode.com/problems/jump-game-ii/
    You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0]. 
    Each element nums[i] represents the maximum length of a forward jump from index i. 
    In other words, if you are at nums[i], you can jump to any nums[i + j] where:
    0 <= j <= nums[i] and i + j < n
    Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
    '''
    def sol1(self, nums: List[int]) -> int:        
        if len(nums) <= 1: return 0
        pos, furthest_pos = 0, nums[0]
        times = 1
        while furthest_pos < len(nums) - 1:
            times += 1
            nxt = max(i + nums[i] for i in range(pos, furthest_pos + 1))
            pos, furthest_pos = furthest_pos, nxt
        return times

    def sol2(self, nums: List[int]) -> int:        
        if len(nums) <= 1: return 0 
        jumps = 0
        max_jump = nums[0] # this is as far as we can jump from origin
        pos = 0      # this is the current index
        while max_jump < (len(nums)-1):
            max_jumpo = max_jump
            for i in range(pos, max_jump+1): # these are all potential future jumps
                if max_jump <= (nums[i]+i):
                    max_jump = (nums[i]+i)
            jumps+=1
            pos = max_jumpo
        return jumps + 1
            
class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.sol1, self.sol2]:
            self.assertEqual(sol([2,3,1,1,4]), 2)
            self.assertEqual(sol([2,3,0,1,4]), 2)
            self.assertEqual(sol([1,3,2]), 2)
            self.assertEqual(sol([2,3,1]), 1)
            self.assertEqual(sol([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]), 2)

if __name__ == "__main__":
    unittest.main()
