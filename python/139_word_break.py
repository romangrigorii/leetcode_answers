import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    139: https://leetcode.com/problems/word-break
    Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
    '''
    def sol1(self, s: str, wordDict: List[str]) -> bool:
        d = [False]*len(s)
        for i in range(len(s)):
            for w in wordDict:
                if s[i-len(w)+1:].startswith(w) and (i<len(w) or d[i-len(w)]):
                    d[i] = True
                    break
        return d[-1]

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol("leetcode", ["leet","code"]), True)
            self.assertEqual(sol("applepenapple", ["apple","pen"]), True)

if __name__ == "__main__":
    unittest.main()
