import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    64: https://leetcode.com/problems/minimum-path-sum/description/
    Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes 
    the sum of all numbers along its path.
    Note: You can only move either down or right at any point in time.
    '''
    def minPathSum(self, grid: List[List[int]]) -> int:
        r = len(grid)
        l = len(grid[0])
        for r_ in range(1, r):
            grid[r_][0]+= grid[r_-1][0]
        for l_ in range(1, l):
            grid[0][l_]+= grid[0][l_-1]
        for r_ in range(1,r):
            for l_ in range(1,l):
                grid[r_][l_] += min(grid[r_-1][l_], grid[r_][l_-1])
        return grid[-1][-1]
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.minPathSum]:
            self.assertEqual(sol([[1,3,1],[1,5,1],[4,2,1]]), 7)

if __name__ == "__main__":
    unittest.main()
    