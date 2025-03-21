import unittest
from typing import Optional, List
from helpers import *

class _ (Helpers):
    '''
    7: https://leetcode.com/problems/reverse-integer/description/
    Given a signed 32-bit integer x, return x with its digits reversed. 
    If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
    123 -> 321
    -123 -> -321
    '''
    def sol1(self, x: int) -> int:
        lim_hi = 2**31 -1
        lim_lo = -2**31
        out = 0
        if x:
            neg = x<0
            if neg:
                x *= -1
            pow = int(log10(x))
            for p in range(pow,-1,-1):
                k = int(x/(10**p))
                if k:
                    x -= int(x/(10**p))*(10**p)
                    out += 10**(pow-p)*k
            if neg:
                out *= -1
            if out<lim_lo or out>lim_hi:
                out = 0
        return out
    
class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        self.assertEqual(self.sol1(123), 321)
        self.assertEqual(self.sol1(-123), -321)

if __name__ == "__main__":
    unittest.main()