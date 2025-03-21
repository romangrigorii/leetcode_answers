import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    74: https://leetcode.com/problems/search-a-2d-matrix/
    Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
    You must do it in place.
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rm = len(matrix)
        cm = len(matrix[0])
        s = 0
        e = rm*cm - 1
        while s<=e:
            m = (s+e)//2
            r = m//cm
            c = m%cm
            if target < matrix[r][c]:
                e = m - 1
            elif target > matrix[r][c]:
                s = m + 1
            else:
                return True
        return False

class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.searchMatrix]:
            self.assertEqual(sol([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3),True)

if __name__ == "__main__":
    unittest.main()
