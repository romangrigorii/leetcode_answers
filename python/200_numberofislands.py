import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    200: https://leetcode.com/problems/number-of-islands
    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
    You may assume all four edges of the grid are all surrounded by water.
    '''
    def sol1(self, grid: List[List[str]]) -> int:
        islands = set()
        islandnum = set()
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        R = len(grid)
        C = len(grid[0])

        def helper(pos, islands, islandtie):
            if grid[pos[0]][pos[1]] == "0": # if water
                islands.add(pos)
                return
            if pos in islands: # if visited
                return
            islands.add(pos)
            islandnum.add(islandtie)           
            for d in directions:
                new_pos = (pos[0]+d[0], pos[1]+d[1])
                if new_pos[0]>=0 and new_pos[0]<R and new_pos[1]>=0 and new_pos[1]<C:
                    helper(new_pos, islands, islandtie)
            
        for r in range(R):
            for c in range(C):
                helper((r,c), islands, (r,c))
        return len(islandnum)

    def sol2(self, grid):
        def dfs(self, grid, i, j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = '#' # mark islands that were visited 
            self.dfs(grid, i+1, j)
            self.dfs(grid, i-1, j)
            self.dfs(grid, i, j+1)
            self.dfs(grid, i, j-1)
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol(grid = [["1","1","1","1","0"], ["1","1","0","1","0"], ["1","1","0","0","0"], ["0","0","0","0","0"]]), 1)

if __name__ == "__main__":
    unittest.main()
