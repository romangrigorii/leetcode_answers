import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    62: https://leetcode.com/problems/unique-paths/description/
    There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
    The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
    The robot can only move either down or right at any point in time.
    Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
    The test cases are generated so that the answer will be less than or equal to 2 * 10^9.
    '''
    def uniquePaths(self, m: int, n: int) -> int:
        out = [[1]*n for k in range(m)]
        for m_ in range(1,m):
            for n_ in range(1,n):
                out[m_][n_] = out[m_-1][n_] + out[m_][n_-1]
        return out[-1][-1]
   
class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.uniquePaths]:
            self.assertEqual(sol(3,7), 28)
            self.assertEqual(sol(6,2), 6)

if __name__ == "__main__":
    unittest.main()
    