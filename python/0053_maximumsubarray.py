import unittest
from typing import Optional, List
from helpers import *

class Maximum_Subarray():
    '''
    53: https://leetcode.com/problems/maximum-subarray
    Given an integer list nums, find the maximum value to which the subarrays can add to.
    '''
    def sol1(self, nums: List[int]) -> int:
        '''
        This is Kadane's algorithm. The idea is that we add only parts of the array that would contribute positively to our overall sum.
        If our sum so far is negative we 'shed' it. It might be the max thus far, but it will certainly contribute negatively to future
        sums.
        '''
        for i in range(1, len(nums)):
            if nums[i-1]>0:
                nums[i]+=nums[i-1]
        return max(nums)
    
class test(unittest.TestCase, Maximum_Subarray):
    def test_(self):
        self.assertEqual(self.sol1(nums = [-2,1,-3,4,-1,2,1,-5,4]), 6)
        self.assertEqual(self.sol1(nums = [1]), 1)
        self.assertEqual(self.sol1(nums = [5,4,-1,7,8]), 23)

if __name__ == "__main__":
    unittest.main()