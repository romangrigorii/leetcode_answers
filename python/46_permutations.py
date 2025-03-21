import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    46: https://leetcode.com/problems/permutations/description/
    Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
    '''
    def sol1(self, nums: List[int]) -> int:
        out = []
        self.dfs(out, nums, [])
        return out  
    def dfs(self, out, available, current):
        if not available: out.append(current)
        else:
            for i in range(len(available)):
                self.dfs(out, available[:i] + available[i+1:], current + [available[i]])

    def sol2(self, nums: List[int]):
        out = self.sol2_helper(nums)
        return out
    
    def sol2_helper(self, nums):
        if not nums: return [[]]
        if nums:
            out = self.sol2_helper(nums[1:])
            return [q[:i] + [nums[0]] + q[i:] for q in out for i in range(len(q)+1)]


class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        for sol in [self.sol1, self.sol2]:
            self.equal_lists(sol([1,2,3]), [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])

if __name__ == "__main__":
    unittest.main()
