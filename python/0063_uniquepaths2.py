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
    The test cases are generated so that the answer will be less than or equal to 2 * 109.
    '''
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for m_ in range(m):
            if obstacleGrid[m_][0] == 0: 
                obstacleGrid[m_][0] = -1        
            else: break
        for n_ in range(n):
            if obstacleGrid[0][n_] <= 0: 
                obstacleGrid[0][n_] = -1        
            else: break
        for m_ in range(1,m):
            for n_ in range(1,n):
                if obstacleGrid[m_][n_] == 0:
                    obstacleGrid[m_][n_] = (obstacleGrid[m_-1][n_] if obstacleGrid[m_-1][n_]<0 else 0) + (obstacleGrid[m_][n_-1] if obstacleGrid[m_][n_-1]<0 else 0)
        return -obstacleGrid[-1][-1] if obstacleGrid[-1][-1]<0 else 0

    
class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.uniquePathsWithObstacles]:
            self.assertEqual(sol([[0,0,0],[0,1,0],[0,0,0]]), 2)

if __name__ == "__main__":
    unittest.main()
    