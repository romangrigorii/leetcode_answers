import unittest
from typing import Optional, List
from helpers import *
class _ :
    '''
    47: https://leetcode.com/problems/permutations-ii/
    Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
    '''
    def sol1(self, nums: List[int]) -> int:
        nums.sort()
        out = []
        self.dfs(out, nums, [])
        return out  
    def dfs(self, out, available, current):
        if not available: out.append(current)
        else:
            for i in range(len(available)):
                if i>0 and available[i] == available[i-1]: continue
            self.dfs(out, available[:i] + available[i+1:], current + [available[i]])

class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        for sol in [self.sol1]:
            self.equal_lists(sol([1,1,3]), [[1,1,2],[1,2,1],[2,1,1]])

if __name__ == "__main__":
    unittest.main()
