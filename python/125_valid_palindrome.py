import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    125: https://leetcode.com/problems/valid-palindrome/description/
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing 
    all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
    Given a string s, return true if it is a palindrome, or false otherwise.
    '''
    def sol1(self, s: str) -> bool:
        lst = 'abcdefghijklmnoprstquvwxyzABCDEFGHIJKLMNOPRSTQUVXYZ'
        lstf = ''
        for q in s:
            if q in lst: lstf+=q.lower()
        return lstf == lstf[::-1]
    
    def sol2(self, s:str) -> bool:
        s = ''.join(map(lambda x : x.lower() if x.isalpha() or x.isdigit() else '', s))
        n = len(s)
        return s[:(n-1) // 2+1] == s[(n)//2:][::-1]
        
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1, self.sol2]:
            self.assertEqual(sol(s = "A man, a plan, a canal: Panama"), True)


if __name__ == "__main__":
    unittest.main()
