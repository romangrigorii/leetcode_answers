import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    59_https://leetcode.com/problems/spiral-matrix-ii/
    Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
    '''
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0]*n for i in range(n)]
        i,j,di,dj = 0,0,0,1
        for q in range(n*n):
            mat[i][j] = q+1
            if mat[(i+di)%n][(j+dj)%n]:
                di,dj = dj, -di
            i+=di
            j+=dj
        return mat
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.generateMatrix]:
            self.assertEqual(sol(3), [[1,2,3],[8,9,4],[7,6,5]])


if __name__ == "__main__":
    unittest.main()
    