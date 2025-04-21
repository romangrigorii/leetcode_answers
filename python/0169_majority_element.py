import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    169: https://leetcode.com/problems/majority-element/

    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

    '''
    def sol1(self, nums: List[int]) -> int:
        c = Counter(nums)
        return max(c.items(), key = lambda x: x[1])[0]
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol([2,2,1,1,1,2,2]), 2)
            self.assertEqual(sol([3,2,3]), 3)

if __name__ == "__main__":
    unittest.main()
