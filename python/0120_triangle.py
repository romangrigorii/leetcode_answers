import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    120: https://leetcode.com/problems/triangle/description/
    Given a triangle array, return the minimum path sum from top to bottom.
    For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the 
    current row, you may move to either index i or index i + 1 on the next row.
    '''
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for q in range(1,len(triangle)):
            triangle[q][0] += triangle[q-1][0]
            triangle[q][-1] += triangle[q-1][-1]
            for j in range(1,q):
                triangle[q][j]+=min(triangle[q-1][j-1],triangle[q-1][j])
        return min(triangle[-1])
        
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.minimumTotal]:
            self.assertEqual(sol(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]), 11)


if __name__ == "__main__":
    unittest.main()
