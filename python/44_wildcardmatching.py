import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    44:  https://leetcode.com/problems/wildcard-matching/description/
    Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
    '?' Matches any single character.
    '*' Matches any sequence of characters (including the empty sequence).
    The matching should cover the entire input string (not partial).
    '''
    def sol1(self, s, p):
        dp = [[False for _ in range(len(p)+1)] for i in range(len(s)+1)] # this creates a table of booleans associated with completion of particular section of a word
        dp[0][0] = True
        for j in range(1, len(p)+1):
            if p[j-1] != '*':
                break
            dp[0][j] = True # any sequence of characters up to this point could have been consumed - this is the base example
        # note that this [0] refers to the point where no characters from s have been consumed
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] in {s[i-1], '?'}:
                    dp[i][j] = dp[i-1][j-1] # if there is a character match we check if we have matched characters up tp this point
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1] # either we swallow up a previously encountered letter in s and stay with p or we move on past p
        return dp[-1][-1]
    
    def sol2(self, s: str, p: str) -> bool:
        i, j = 0, 0
        last_match, star = 0, -1

        while i < len(s):
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                last_match = i
                star = j
                j += 1
            elif star != -1:
                j = star + 1
                i = last_match + 1
                last_match += 1
            else:
                return False
        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p)

class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        for sol in [self.sol1, self.sol2]:
            self.assertEqual(sol("cb", "?a"), False)
            self.assertEqual(sol("aa", "a"), False)
            self.assertEqual(sol("aa", "*"), True)

if __name__ == "__main__":
    unittest.main()
