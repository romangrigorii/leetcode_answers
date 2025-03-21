import unittest
from typing import Optional, List
from helpers import *

class _ (Helpers):
    '''
    13: https://leetcode.com/problems/roman-to-integer/description/
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
    Given a roman numeral, convert it to an integer.

    '''
    def sol1(self, num: str) -> int:
        strs = {'M' : 1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, "I":1}
        out = 0
        L = len(num)-1
        i = 0
        while i < L+1:
            if (i+1) <=L and strs[num[i+1]]>strs[num[i]]:
                out += strs[num[i+1]] - strs[num[i]]
                i+=2
            else:
                out += strs[num[i]]
                i+=1
        return out
    
    
class test(unittest.TestCase, _ , Helpers):
    def test_1(self):
        self.assertEqual(self.sol1('III'), 3)
        self.assertEqual(self.sol1('LVIII'), 58)
        self.assertEqual(self.sol1('IX'), 9)
        self.assertEqual(self.sol1('MCMXCIV'), 1994)

if __name__ == "__main__":
    unittest.main()