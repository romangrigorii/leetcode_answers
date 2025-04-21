import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    119: https://leetcode.com/problems/pascals-triangle-ii/
    Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle. 
    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
    '''
    def getRow(self, rowIndex: int) -> List[int]:
        out = []
        for i in range(rowIndex):
            out = [out[0]] + [out[q] + out[q+1] for q in range(len(out)-1)] + [out[-1]] if out else [1]
        return out
                
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.getRow]:
            self.assertEqual(sol(5), [1,4,6,4,1])


if __name__ == "__main__":
    unittest.main()
