import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    115: https://leetcode.com/problems/distinct-subsequences/description/
    Given two strings s and t, return the number of distinct subsequences of s which equals t.
    The test cases are generated so that the answer fits on a 32-bit signed integer.
    '''
    def sol1(self, s: str, t: str) -> int:
        L1 = len(s)-1
        L2 = len(t)-1
        def helper(p1,p2):
            if p1>L1: return 0
            if p2 == L2: return s[p1] == t[p2]
            if s[p1] == t[p2]: 
                return helper(p1+1,p2) + helper(p1+1,p2+1)
            return helper(p1+1,p2)
        return helper(0,0)

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:            
            self.assertEqual(sol("rabbbit","rabbit"), 3)



if __name__ == "__main__":
    unittest.main()
