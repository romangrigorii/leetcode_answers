import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    162: https://leetcode.com/problems/find-peak-element/description/
    A peak element is an element that is strictly greater than its neighbors.

    Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

    You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

    You must write an algorithm that runs in O(log n) time.

    '''
    def sol1(self, lst: List[int]) -> int:
        start, end = 0, len(lst) - 1
        while start < end:
            mid = start + (end - start) // 2
            if lst[mid] > lst[mid + 1]:
                end = mid
            else:
                start = mid + 1
        return start
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol([1,2,3,1]), 2)
            self.assertEqual(sol([1,2,1,3,5,6,4]), 5)

if __name__ == "__main__":
    unittest.main()
