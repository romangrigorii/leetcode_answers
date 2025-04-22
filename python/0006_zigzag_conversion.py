import unittest
from typing import Optional, List
from helpers import *

class _ (Helpers):
    '''
    6: https://leetcode.com/problems/zigzag-conversion/
    '''
    def sol1(self, s: str, numRows: int) -> str:
        out = ""
        if len(s):
            for r in range(numRows,0,-1):
                s1 = (r-1)*2
                s2 = (numRows-r)*2
                sk = 0
                p = numRows - r # we start at 0
                while (p+sk)<len(s):
                    p+=sk
                    out += s[p]
                    if not s1 and not s2:
                        sk = 1
                    elif s1 and (sk==s2 or sk == 0):
                        sk = s1
                    elif s2 and sk==s1:
                        sk = s2
        return out

class test(unittest.TestCase, _, Helpers):
    def test_(self):
        self.assertEqual(self.sol1("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
        self.assertEqual(self.sol1("PAYPALISHIRING", 4), "PINALSIGYAHRPI")
        self.assertEqual(self.sol1("A", 1), "A")

if __name__ == "__main__":
    unittest.main()
