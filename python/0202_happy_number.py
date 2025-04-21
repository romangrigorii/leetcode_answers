import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    202: https://leetcode.com/problems/happy-number/
    Write an algorithm to determine if a number n is happy.

    A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.
    Return true if n is a happy number, and false if not.
    '''
    def sol1(self, n: int) -> int:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum([int(x) **2 for x in str(n)])
        return n == 1

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol(19), True)
            self.assertEqual(sol(2), False)

if __name__ == "__main__":
    unittest.main()
