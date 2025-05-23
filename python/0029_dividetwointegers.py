import unittest
from typing import Optional, List
from helpers import *

class _ (ListNode):
    '''
    27: https://leetcode.com/problems/divide-two-integers/
    Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
    The integer division should truncate toward zero, which means losing its fractional part. 
    For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
    Return the quotient after dividing dividend by divisor. 
    Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. 
    For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.
    '''
    def sol1(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend < 0) != (divisor < 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = len(range(0, dividend-divisor+1, divisor))
        if sign == -1:
            result = -result
        minus_limit = -(2**31)
        plus_limit = (2**31 - 1)
        result = min(max(result, minus_limit), plus_limit)
        return result 

 
class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        self.assertEqual(self.sol1(10, 3), 3)
        self.assertEqual(self.sol1(7, -3), -2)

if __name__ == "__main__":
    unittest.main()