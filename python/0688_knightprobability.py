import unittest
from typing import Optional, List
from helpers import *
import numpy as np

class _ :
    '''
    688: https://leetcode.com/problems/knight-probability-in-chessboard/description/
    The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).
    A chess knight has eight possible moves it can make, as illustrated below. 
    Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.
    Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.
    The knight continues moving until it has made exactly k moves or has moved off the chessboard.
    Return the probability that the knight remains on the board after it has stopped moving.
    '''
    def sol1(self, n: int, k: int, row: int, column: int) -> float:
        prob = [[0]*n for i in range(n)]
        prob[row][column] = 1
        moves = [(-2,-1),(-1,-2),(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1)]
        for i in range(k):
            prob_new = [[0]*n for i in range(n)]
            for r in range(n):
                for c in range(n):
                    for m in moves:
                        if m[0]+r>=0 and m[0]+r<n and m[1]+c>=0 and m[1]+c<n:
                            prob_new[r][c] += .125*prob[m[0]+r][m[1]+c]
            prob = prob_new
        return np.sum(np.array(prob))

class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.sol1]:
            self.assertEqual(sol(3,1,0,0), .25)
            self.assertEqual(sol(5,5,0,0), .0224609375)

if __name__ == "__main__":
    unittest.main()
