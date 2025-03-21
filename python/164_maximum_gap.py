import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    160: https://leetcode.com/problems/intersection-of-two-linked-lists/
    Given an integer array nums, return the maximum difference between two successive elements in its sorted form. 
    If the array contains less than two elements, return 0.

    You must write an algorithm that runs in linear time and uses linear extra space.

    '''
    def sol1(self, nums: List[int]) -> int:
        hi, lo, L = max(nums), min(nums), len(nums)
        if len(nums)<= 2 or hi == lo: return hi - lo
        out = defaultdict(list)
        for n in nums:
            ind = L-2 if n == hi else (n-lo)*(L-1)//(hi-lo)
            out[ind].append(n)
        candidates = [[min(out[i]), max(out[i])] for i in range(L-1) if out[i]]
        return max([candidates[i][0] - candidates[i-1][1] for i in range(1,len(candidates))])
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol([3,6,9,1]), 3)

if __name__ == "__main__":
    unittest.main()
