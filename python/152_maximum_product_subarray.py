import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    152: https://leetcode.com/problems/maximum-product-subarray/description/
    Given an array of numbers, find the largest product of a subarray of said array.
    '''
    def sol1(self, A):
        B = A[::-1] # we take the array in reverse
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1 # 
            B[i] *= B[i - 1] or 1
        return max(A + B)
    
    def sol2(self, nums: List[int]) -> int:
        '''
        This solution is similar to sol1 but relies on finding concurrent max rather than max of two multiplied arrays.
        It's more efficient and easier to understand.
        '''
        prefix, suffix, max_so_far = 0, 0, float('-inf')
        for i in range(len(nums)):
            prefix = (prefix or 1) * nums[i] # this traverses the array rightward and resets when a 0 is found
            suffix = (suffix or 1) * nums[~i] # this traverses the array leftward and resets when a 0 is found
            max_so_far = max(max_so_far, prefix, suffix)
        return max_so_far

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol([2,3,-2,4]), 6)
            self.assertEqual(sol([-2,0,-1]), 0)

if __name__ == "__main__":
    unittest.main()
