import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    90: https://leetcode.com/problems/subsets-ii/description/
    Given an integer array nums that may contain duplicates, return all possible subsets (the power set). 
    The solution set must not contain duplicate subsets. Return the solution in any order.
    '''
    def subsetsWithDup(self, nums):
        ret = []
        self.dfs(sorted(nums), [], ret)
        return ret
    
    def dfs(self, nums, path, ret):
        ret.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[i+1:], path+[nums[i]], ret)


class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.subsetsWithDup]:
            self.assertEqual(sol([1,2,2]), [[],[1],[1,2],[1,2,2],[2],[2,2]])
if __name__ == "__main__":
    unittest.main()
