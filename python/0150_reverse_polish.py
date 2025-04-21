import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    150: https://leetcode.com/problems/evaluate-reverse-polish-notation/
    You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

    Evaluate the expression. Return an integer that represents the value of the expression.

    Note that:

    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.
    '''
    def minimumTotal(self, tokens: List[str]) -> int:
        stack = []
        for q in tokens:
            if q not in "+-*/":
                stack.append(int(q))
            else:
                r, l = stack.pop(), stack.pop()
                if q == "+": stack.append(l+r)
                elif q =="-": stack.append(l-r)
                elif q == "*": stack.append(l*r)
                else: stack.append(int(float(l)/r))
        return stack.pop()
        
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.minimumTotal]:
            self.assertEqual(sol(["2","1","+","3","*"]), 9)
            self.assertEqual(sol(["4","13","5","/","+"]), 6)

if __name__ == "__main__":
    unittest.main()
