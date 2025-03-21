import unittest
from typing import Optional, List
from helpers import *

class _ (Helpers):
    '''
    9 : https://leetcode.com/problems/palindrome-number/
    Given an integer x, return true if x is a palindrome, and false otherwise.
    '''
    def sol1(self, x: int) -> int:
        s = str(x)
        l = 0
        e = len(s)-1
        while l<e: 
            if s[l]==s[e]:
                l+=1
                e-=1
            else:
                return False
        return True

            
    
class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        self.assertEqual(self.sol1(121), True)
        self.assertEqual(self.sol1(-121), False)

if __name__ == "__main__":
    unittest.main()