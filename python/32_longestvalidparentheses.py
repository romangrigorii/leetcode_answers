import unittest
from typing import Optional, List
from helpers import *

class _ (ListNode):
    '''
    32: https://leetcode.com/problems/longest-valid-parentheses/description/
    Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) 
    parentheses substring
    '''
    def sol1(self, s: str) -> int:
        dp, stack = [0]*(1+len(s)), []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i) # the last time '(' was encountered
            else:
                if stack:
                    last = stack.pop()
                    dp[i+1] = dp[last] + i - last + 1
        return max(dp) 
       
 
class test(unittest.TestCase, _, ListNode):
    def test_1(self):
        self.assertEqual(self.sol1('(()'), 2)
        self.assertEqual(self.sol1(')()())'), 4)

if __name__ == "__main__":
    unittest.main()