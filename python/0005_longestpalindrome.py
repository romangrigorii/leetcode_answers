import unittest
from typing import Optional, List
from helpers import *

class _ (Helpers):
    '''
    5: https://leetcode.com/problems/longest-palindromic-substring/
    '''
    def sol1(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            res = max(self.sol1_helper(s,i,i), self.sol1_helper(s,i,i+1), res, key = len)
        return res

    def sol1_helper(self,s, pos1, pos2):
        while (pos1>=0 and pos2<len(s) and s[pos1]==s[pos2]):
            pos1-=1
            pos2+=1
        return s[pos1+1:pos2]

class test(unittest.TestCase, _, Helpers):
    def test_(self):
        self.assertEqual(self.sol1("babad"), "aba")
        self.assertEqual(self.sol1("cbbd"), "bb")

if __name__ == "__main__":
    unittest.main()
