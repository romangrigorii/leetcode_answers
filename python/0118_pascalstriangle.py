import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    118: https://leetcode.com/problems/pascals-triangle/
    Given an integer numRows, return the first numRows of Pascal's triangle.
    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
    '''
    def generate(self, numRows: int) -> List[List[int]]:
        out = []
        for i in range(numRows):
            out += [[out[-1][0]] + [out[-1][q] + out[-1][q+1] for q in range(len(out[-1])-1)] + [out[-1][-1]] if out else [1]]
        return out
                
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.generate]:
            self.assertEqual(sol(5), [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])


if __name__ == "__main__":
    unittest.main()
