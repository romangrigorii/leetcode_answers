import unittest
from typing import Optional, List
from helpers import *

class _ (Helpers):
    '''
    19: https://leetcode.com/problems/valid-parentheses/
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
    '''
    def sol1(self, s: str) -> bool:
        stack = []
        dict = {']':'[', ')':'(', '}': '{'}
        opens = '[({'
        closes = ')}]'
        for q in s:
            if q in opens:
                stack.append(q)
            elif q in closes:
                if not stack or dict[q] != stack.pop(): 
                    return False
            else: return False
        return stack == []

 
class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        self.assertEqual(self.sol1(s = "()"), True)
        self.assertEqual(self.sol1(s = "()[]{}"), True)
        self.assertEqual(self.sol1(s = "(]"), False)

if __name__ == "__main__":
    unittest.main()