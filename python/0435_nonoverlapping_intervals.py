import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    435: https://leetcode.com/problems/non-overlapping-intervals/
    Given an array of intervals where intervals[i] = [starti, endi], 
    return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
    '''
    def sol1(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        cnt = 0
        curmax = float('-inf')
        for i in intervals:
            if i[0]>=curmax: # first time add
                cursmall = i[0]
                curmax = i[1]                
            else:
                cnt+=1
                curmax = min(curmax,i[1])
        return cnt

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol([[1,2],[2,3],[3,4],[1,3]]), 1)

if __name__ == "__main__":
    unittest.main()
