import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    205: https://leetcode.com/problems/isomorphic-strings/
    Given two strings s and t, determine if they are isomorphic.

    Two strings s and t are isomorphic if the characters in s can be replaced to get t.

    All occurrences of a character must be replaced with another character while preserving the order of characters. 
    No two characters may map to the same character, but a character may map to itself.
    '''
    def sol1(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        for i in range(len(s)):
            if d1.setdefault(s[i], t[i]) != t[i] or d2.setdefault(t[i], s[i]) != s[i]: return False
        return True

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol('egg', 'add'), True)
            self.assertEqual(sol('foo', 'bar'), False)
            self.assertEqual(sol('paper', 'title'), True)


if __name__ == "__main__":
    unittest.main()
