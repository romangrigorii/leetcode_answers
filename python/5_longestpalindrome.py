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

class LongestPalindromePractice:
    def longest_palindrome_h(self, s: str, idxl, idxr) -> str:
        e = len(s)-1
        while idxl>=0 and idxr<=e:
            if s[idxl] == s[idxr]:
                idxl -=1
                idxr +=1
            else:
                break
        return s[idxl+1:idxr]

    def longest_palindrome(self, s):
        if not s: return ''
        longest_palindrome = s[0]
        for i in range(len(s)):
            longest_palindrome = max([longest_palindrome, self.longest_palindrome_h(s,i,i), self.longest_palindrome_h(s,i,i+1)], key=len)
        return longest_palindrome

class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        self.assertEqual(self.longest_palindrome("babad"), "bab")
        self.assertEqual(self.longest_palindrome("cbbd"), "bb")

if __name__ == "__main__":
    unittest.main()
