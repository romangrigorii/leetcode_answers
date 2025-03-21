import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    78: https://leetcode.com/problems/subsets/
    Given an integer array nums of unique elements, return all possible subsets (the power set).
    The solution set must not contain duplicate subsets. Return the solution in any order.
    '''
    def sol1(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for q in nums:
            res += [h + [q] for h in res]
        return res
    
    def sol2(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(sofar, left):
            res.append(sofar)
            for n in range(len(left)):
                dfs(sofar + [left[n]], left[n+1:])
        dfs([], nums)
        return res

class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.sol1, self.sol2]:
            self.equal_lists(sol([1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])

if __name__ == "__main__":
    unittest.main()
