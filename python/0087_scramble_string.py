import unittest
from typing import Optional, List
from helpers import *
from collections import Counter

class _(Helpers) :
    '''
    86: https://leetcode.com/problems/scramble-string/
    We can scramble a string s to get a string t using the following algorithm:

    If the length of the string is 1, stop.
    If the length of the string is > 1, do the following:
    Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
    Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
    Apply step 1 recursively on each of the two substrings x and y.
    Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.
 
    '''
    def sol1(self, s1: str, s2: str) -> bool:
        def helper(s,e):
            if e - s == 1: return s1[s] == s2[s]
            if e - s == 2: return Counter(s1[s:e]) == Counter(s2[s:e])
            res = False
            for i in range(s+1,e):
                if Counter(s1[s:i]) == Counter(s2[s:i]):
                    res = res or (helper(s,i) and helper(i,e))
            return res
        return helper(0,len(s1))
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.sol1]:
            self.assertEqual(sol("great", "rgeat"), True)
            self.assertEqual(sol("abcde", "caebd"), False)

if __name__ == "__main__":
    unittest.main()
