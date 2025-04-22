import unittest
from typing import Optional, List
from helpers import *

class _ (Helpers):
    '''
    8: https://leetcode.com/problems/string-to-integer-atoi/description/
    Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

    The algorithm for myAtoi(string s) is as follows:

    Whitespace: Ignore any leading whitespace (" ").
    Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
    Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
    Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
    Return the integer as the final result.
    '''
    def sol1(self, s: str) -> int:
        s = s.strip()  # Remove leading/trailing spaces
        if not s:
            return 0
        sign, i, res = 1, 0, 0
        # Check for sign
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            # Handle overflow
            if sign * res > 2**31 - 1:
                return 2**31 - 1
            if sign * res < -2**31:
                return -2**31
            i += 1

        return sign * res
    
class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        self.assertEqual(self.sol1("42"), 42)
        self.assertEqual(self.sol1("   -042"), -42)
        self.assertEqual(self.sol1("0-1"), 0)
        self.assertEqual(self.sol1("words and 987"), 0)

if __name__ == "__main__":
    unittest.main()