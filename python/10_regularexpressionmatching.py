import unittest
from typing import Optional, List
from helpers import *

class _ (Helpers):
    '''
    10: https://leetcode.com/problems/regular-expression-matching/solutions/192023/6-lines-in-python/
    Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
    '.' Matches any single character.
    '*' Matches zero or more of the preceding element.
    The matching should cover the entire input string (not partial).
    '''
    def sol1(self, s, p):
        '''
        Note that we use both recursive and dp solution here.
        In the case whhere s = "" and p = '***...*" this is o(p) time and O(p) space
        Othwerwise this is O(n*m) time and O(n*m) auxiliary space
        '''
        memo = {} # we store indeces of s and p to check if have already looked at them
        def dp(si, pi): # pi represents the index
            if pi == len(p): return si == len(s) # if we have reached the end of p, we better have also reached the end of s
            if si == len(s): # if we have reached the end of s we check if there are wildcard characters left in p
                return pi + 1 < len(p) and p[pi + 1] == '*' and dp(si, pi + 2)
            if (si, pi) not in memo: # if we haven't visited the s and p pair yet
                matched = p[pi] == '.' or p[pi] == s[si]
                if pi + 1 < len(p) and p[pi + 1] == '*':
                    memo[(si, pi)] = dp(si, pi + 2) or (matched and dp(si + 1, pi)) # we either eat the wildcard or move on in s
                else:
                    memo[(si, pi)] = matched and dp(si + 1, pi + 1)
            return memo[(si, pi)]
        return dp(0, 0)

    def sol2(self, s, p):
        if not p: # if there are no more p characters to match, we better have exhausted s as well
            return not s
        if not s: # if we have exhausted the string but there are more values to go through in p. 
            # the only thing p is allowed to have is x* characters as they can correspond to empty chars
            return len(p) > 1 and p[1] == '*' and self.sol2(s, p[2:])
        Matched = (p[0] == '.' or p[0] == s[0])
        if len(p) > 1 and p[1] == '*':
            return (Matched and self.sol2(s[1:], p)) or self.sol2(s, p[2:])
            # if we matched the character and there is a * in p[1] it means we can match any numner of additional characters in s, 
            # we so recusrively search the rest of s while keeping p intact
            # we can also have reached the end point of matching, and will now bypass the wild chaarcter of p
        return Matched and self.sol2(s[1:], p[1:])
            # the default mathching case is that we just continue on with the match
            
    
class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        for sol in [self.sol1, self.sol2]:
            self.assertEqual(sol("aa","a"), False)
            self.assertEqual(sol("aa","a*"), True)
            self.assertEqual(sol("ab",".*"), True)

if __name__ == "__main__":
    unittest.main()