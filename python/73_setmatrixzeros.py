import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    73: https://leetcode.com/problems/set-matrix-zeroes/description/
    Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
    You must do it in place.

    '''
    def setZeroes(self, matrix: List[List[int]]) -> None:
        '''
        The idea is to create a seperate set of all matrix entries which will need to be zeros out
        '''
        to_set = set()
        for ri, r in enumerate(matrix):
            for ci, c in enumerate(r):
                if matrix[ri][ci] == 0:
                    s = set([(q, ci) for q in range(len(matrix))] + [(ri, q) for q in range(len(matrix[0]))])
                    to_set |= s
        for p in to_set:
            matrix[p[0]][p[1]] = 0
        return matrix

class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.setZeroes]:
            self.assertEqual(sol([[1,1,1],[1,0,1],[1,1,1]]), [[1,0,1],[0,0,0],[1,0,1]])

if __name__ == "__main__":
    unittest.main()
