import sys
sys.path.insert(0, "..")
sys.path.insert(0, "../..")
import unittest
from typing import Optional, List
from helpers import *
import numpy as np

class _ (Helpers):
    '''
    1: 
    Given an array of n integers where nums[i] is in the range [1, n]
    return an array of all the integers in the range [1, n] that do not appear in nums.
    '''
    def sol1(self, nums) -> bool:
        L = len(nums)
        nums = list(set(nums))
        nums.sort()
        offset = 0
        out = []
        for i in range(L):
            if nums[i-offset] != i+1: 
                out.append(i+1)
                offset+=1
        return out

        

class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        for sol in [self.sol1]:
            self.assertEqual(sol([4,3,2,7,8,2,3,1]),[5,6])
unittest.main()

# # #              Big-O analysis
# Time O(N)  : as the function will sweep through every element 
# Space O(N) : since at worst we will store N keys and their associated values 