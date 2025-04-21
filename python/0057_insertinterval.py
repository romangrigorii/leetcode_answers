import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    56: https://leetcode.com/problems/insert-interval/
    You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
    represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
    You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
    Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals
    still does not have any overlapping intervals (merge overlapping intervals if necessary).
    Return intervals after the insertion.
    Note that you don't need to modify intervals in-place. You can make a new array and return it.
    '''
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
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
        for sol in [self.insert]:
            self.assertEqual(sol([[1,3],[6,9]], [2,5]), [[1,5],[6,9]])
            self.assertEqual(sol([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]), [[1,2],[3,10],[12,16]])
            self.assertEqual(sol([[1,5]], [0,3]), [[0,5]])


if __name__ == "__main__":
    unittest.main()
