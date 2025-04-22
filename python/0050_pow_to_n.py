import unittest
from typing import Optional, List
from helpers import *
from collections import Counter
class _ :
    '''
    50: https://leetcode.com/problems/powx-n/
    Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
    '''
    def sol1(self, x, n):
        ispos, n = n > 0, abs(n)
        res = 1
        while n != 0:
            mul = x
            tempn = 1
            while n>(tempn<<1):
                mul*=mul
                tempn<<=1
            res*= mul
            n -= tempn

        if ispos:
            return res
        return 1/res

class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        for sol in [self.sol1]:
            self.assertAlmostEqual(sol(2.000, 10), 1024.000)

if __name__ == "__main__":
    unittest.main()
