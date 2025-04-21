import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    128: https://leetcode.com/problems/longest-consecutive-sequence
    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
    You must write an algorithm that runs in O(n) time.
    '''
    def sol1(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0
        checked = set()        
        for x in nums:
            if x - 1 not in nums and x not in checked: # if there is not one smaller, if there is we will get to it so we skip the next steps 
                y = x + 1         # x is the START of the sequence of the previous conditon is false 
                while y in nums: 
                    checked.add(y)
                    y += 1
                best = max(best, y - x)
        return best

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol([100,4,200,1,3,2]), 4)
            self.assertEqual(sol([0,3,7,2,5,8,4,6,0,1]), 9)

if __name__ == "__main__":
    unittest.main()
