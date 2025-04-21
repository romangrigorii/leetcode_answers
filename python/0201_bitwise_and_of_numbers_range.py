import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    201: https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
    Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

    '''
    def sol1(self, left: int, right: int) -> int:
        shift = 0
        while (left != right):
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol(5, 7), 4)
            self.assertEqual(sol(0,0), 0)
            self.assertEqual(sol(1, 1245123), 0)

if __name__ == "__main__":
    unittest.main()
