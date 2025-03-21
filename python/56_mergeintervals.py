import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    56: https://leetcode.com/problems/merge-intervals/
    Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and 
    return an array of the non-overlapping intervals that cover all the intervals in the input.
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key = lambda x: x[0])
        out = [intervals[0]]
        for i in intervals[1:]:
            if i[0] <= out[-1][1]:
                out[-1][1] = max(out[-1][1], i[1])
            else:
                out.append(i)
        return out

    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<2: return intervals        
        intervals = sorted(intervals, key = lambda x: x[0])
        out = [intervals[0]]
        for q in range(1, len(intervals)):
            if out[-1][1]>=intervals[q][0]:
                out[-1][1] = max(intervals[q][1], out[-1][1])
            else:
                out.append(intervals[q])
        return out

        
class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.merge, self.merge2]:
            self.assertEqual(self.merge([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])
            self.assertEqual(self.merge([[1,4],[4,5]]), [[1,5]])

if __name__ == "__main__":
    unittest.main()
