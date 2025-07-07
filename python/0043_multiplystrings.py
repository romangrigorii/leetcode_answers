import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    43:  https://leetcode.com/problems/multiply-strings/
    Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, 
    also represented as a string.
    Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
    '''
    def multiply(self, num1: str, num2: str) -> str:
        product = [0] * (len(num1) + len(num2))
        pos = len(product)-1
        for a in reversed(num1):
            tpos = pos
            for b in reversed(num2):
                product[tpos] += int(a)*int(b)
                product[tpos-1] += int(product[tpos]/10)
                product[tpos] %= 10
                tpos -= 1
            pos -=1
        while len(product)>1 and product[0] == 0:
            product = product[1:]
        return ''.join(map(str, product))

    def multiply2(self, num1: str, num2: str) -> str:
        out = 0
        for i, a in enumerate(reversed(num1)):
            sofar = 0
            for j, b in enumerate(reversed(num2)):
                sofar += int(a)*int(b)*(10**j)
            out+=sofar*(10**i)
        return str(out)

class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        self.assertEqual(self.multiply('2', '3'), '6')
        self.assertEqual(self.multiply('123', '456'), '56088')

if __name__ == "__main__":
    unittest.main()
