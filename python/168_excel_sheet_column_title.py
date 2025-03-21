import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    165: https://leetcode.com/problems/excel-sheet-column-title/description/

    Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

    For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
    

    Example 1:

    Input: columnNumber = 1
    Output: "A"
    Example 2:

    Input: columnNumber = 28
    Output: "AB"
    Example 3:

    Input: columnNumber = 701
    Output: "ZY"

    '''
    def sol1(self, columnNumber: int) -> str:
        result = ''
        distance = ord('A') 

        while columnNumber > 0:
            y = (columnNumber-1) % 26
            columnNumber = (columnNumber-1) // 26
            s = chr(y+distance)
            result = ''.join((s, result))

        return result
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol(1), "A")
            self.assertEqual(sol(701), "ZY")

if __name__ == "__main__":
    unittest.main()
