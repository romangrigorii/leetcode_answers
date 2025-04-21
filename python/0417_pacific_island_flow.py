import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    417: https://leetcode.com/problems/pacific-atlantic-water-flow
    
    There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches 
    the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

    The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] 
    represents the height above sea level of the cell at coordinate (r, c).

    The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and 
    west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent 
    to an ocean into the ocean.

    Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to 
    both the Pacific and Atlantic oceans.
    '''
    def sol1(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return heights
        R, C = len(heights), len(heights[0])
        P_v = set()
        A_v = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def traverse(i, j, visited):            
            if (i,j) in visited:
                return
            visited.add((i,j))
            for d in directions:
                x, y = i+d[0], j+d[1]
                if x>=0 and x<R and y>=0 and y<C and heights[x][y]>=heights[i][j]:
                    traverse(x,y,visited)
        for r in range(R):
            traverse(r,0,P_v)
            traverse(r,C-1,A_v)
        for c in range(C):
            traverse(0,c,P_v)
            traverse(R-1,c,A_v)
        return [list(q) for q in (A_v & P_v)]

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.equal_lists(sol(heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]), [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]])

if __name__ == "__main__":
    unittest.main()
