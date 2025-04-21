import unittest
from typing import Optional, List
from helpers import *
class _ :
    '''
    48: https://leetcode.com/problems/rotate-image/
    You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
    '''
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(len(matrix)):
            for j in range(len(matrix)//2):
                 matrix[i][j], matrix[i][~j] = matrix[i][~j],  matrix[i][j]
        return matrix

class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        for sol in [self.rotate]:
            self.equal_lists(sol([[1,2,3],[4,5,6],[7,8,9]]), [[7,4,1],[8,5,2],[9,6,3]])

if __name__ == "__main__":
    unittest.main()
