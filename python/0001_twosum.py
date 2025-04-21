import unittest
from typing import Optional, List
from helpers import *
import numpy as np
class _ (Helpers):
    '''
    1: https://leetcode.com/problems/two-sum/description/
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    '''
    def sol1(self, nums: List[int], target: int) -> List[int]:
        '''
        This is a classic O(n) solution 
        '''
        d = {}
        for i, q in enumerate(nums):
            if q in d: return [d[q], i]
            else: d[target - q] = i
    
    def sol2(self, nums: List[int], target: int) -> List[int]:
        '''
        This is an iterative solution that is O(NlogN) runtime because of sort
        '''        
        indeces_nums = sorted(enumerate(nums), key = lambda x: x[1])
        l = 0
        r = len(nums)-1
        while l<r:
            s = indeces_nums[l][1] + indeces_nums[r][1] 
            if s == target: return [indeces_nums[l][0], indeces_nums[r][0]]
            elif s < target: l+=1
            else: r-=1
        return -1

class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        for sol in [self.sol1, self.sol2]:
            self.assertEqual(sol(nums = [2,7,11,15], target = 9), [0,1])
            self.assertEqual(sol(nums = [3,2,4], target = 6), [1,2])
            self.assertEqual(sol(nums = [3,3], target = 6), [0,1])

unittest.main()

# # #              Big-O analysis
# Time O(N)  : as the function will sweep through every element 
# Space O(N) : since at worst we will store N keys and their associated values 