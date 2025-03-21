import unittest
from typing import Optional, List
from helpers import *

class Maximum_Subarray():
    '''
    54: https://leetcode.com/problems/spiral-matrix/
    Given an m x n matrix, return all elements of the matrix in spiral order.
    '''
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        r = matrix[0]
        return r + self.spiralOrder([list(q) for q in zip(*matrix[1:])][::-1])
    
class test(unittest.TestCase, Maximum_Subarray):
    def test_(self):
        self.assertEqual(self.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]), [1,2,3,6,9,8,7,4,5])

if __name__ == "__main__":
    unittest.main()