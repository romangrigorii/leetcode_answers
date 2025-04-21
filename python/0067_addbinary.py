import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    66: https://leetcode.com/problems/add-binary/description/
    Given two binary strings a and b, return their sum as a binary string.
    '''
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''
        a = list(a)
        b = list(b)
        while a or b or carry:
            if a: carry += int(a.pop())
            if b: carry += int(b.pop())
            result += str(carry%2)
            carry //= 2
        return result[::-1]

    
class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.addBinary]:
            self.assertEqual(sol(a = "11", b = "1"),"100")
            self.assertEqual(sol(a = "1010", b = "1011"),"10101")

if __name__ == "__main__":
    unittest.main()
