import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    190: https://leetcode.com/problems/reverse-bits/
    Gven a number, reverse its bits
    '''
    def sol1(self, n: int) -> int:
        o = 0
        for i in range(32):
            o <<= 1 # we bit-shift by 1
            o |= (n & 1) # we check if n has a 1 on the right most side and set o accordinfly
            n >>= 1 # we bitshift n to the right
        return o

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol(int(b'00000010100101000001111010011100', 2)), int(b'00111001011110000010100101000000', 2))

if __name__ == "__main__":
    unittest.main()
