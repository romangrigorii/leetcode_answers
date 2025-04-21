import unittest
from typing import Optional, List
from helpers import *

class _ (Helpers):
    '''
    12: https://leetcode.com/problems/integer-to-roman/
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
    Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
    Given an integer, convert it to a roman numeral.

    '''
    def sol1(self, num: int) -> str:
        vals = [1000, 500, 100, 50, 10, 5, 1]
        strs = ['M', 'D', 'C', 'L', 'X', 'V', "I"]
        ind = 0
        out = ''
        while num:            
            if (num - vals[ind]) >=0:
                out += strs[ind] # add most significant number
                num -= vals[ind]
            else:
                ind+=1
            if len(out)>=4 and out[-4:] == 4*strs[ind]: # when we add 4 of the same value, we can just substract 1 from the value that more significant than it
                if len(out)>=5 and out[-5] == strs[ind-1]:
                    out = out[:-5] + strs[ind] + strs[ind-2]
                else:
                    out = out[:-3] + strs[ind-1]
        return out

    def sol2(self, num: int) -> str:
        '''
        Dirty trick method = we basically write out every possible unique set of characters which represent a number.
        '''
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hrns = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        ths = ["", "M", "MM", "MMM"]
        return ths[num//1000] + hrns[(num%1000)//100] + tens[(num%100)//10] + ones[num%10]
    
class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        for sol in [self.sol1, self.sol2]:
            self.assertEqual(sol(3), 'III')
            self.assertEqual(sol(58), 'LVIII')
            self.assertEqual(sol(9), 'IX')
            self.assertEqual(sol(1994), 'MCMXCIV')


if __name__ == "__main__":
    unittest.main()