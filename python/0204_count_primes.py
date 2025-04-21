import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    204: https://leetcode.com/problems/count-primes/
    Given an integer n, return the number of prime numbers that are strictly less than n.
    '''
    def sol1(self, n: int) -> int:
        if n < 2:
            return 0
        s, limit = [1]*n, int(n**0.5) + 1
        s[0] = s[1] = 0
        for i in range(2, limit):
            if s[i] == 1:
                s[i*i:n:i] = [0]*len(s[i*i:n:i])
        return sum(s)

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol(10), 4)
            self.assertEqual(sol(0), 0)
            self.assertEqual(sol(1), 0)


if __name__ == "__main__":
    unittest.main()
