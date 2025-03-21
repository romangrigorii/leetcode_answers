import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    224: https://leetcode.com/problems/basic-calculator/description/
    Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
    Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
    '''
        
    def calculate(self, s) -> int:  
        ressum, currentn, sign, stack = 0, 0, 1, []
        # ressum is total sum
        # currentn is the current number being worked on
        # sign is the current sign applied to curretn
        # stack is the stack of values to be processed
        for char in s:
            if char.isdigit():
                currentn = currentn * 10 + int(char)
            elif char in '+-':
                ressum += currentn * sign # we apply the sign and add it to the ressum
                sign = -1 if char == "-" else 1
                currentn = 0
            elif char == "(":
                stack.append(ressum) # whatever we computer so far we append
                stack.append(sign)
                ressum, sign = 0, 1
            elif char == ")":
                ressum += currentn * sign
                ressum *= stack.pop()
                ressum += stack.pop()
                currentn = 0
        return ressum + (currentn * sign)

    def calculate2(self, s) -> int:
        cur, tot, stack, sgn = 0, 0, [], 1 # tot keeps track of sum between paranthesis and cur keep track of individual values
        for q in s:
            if q.isdigit():
                cur = cur*10 + int(q)
            if q in '+-':
                tot += sgn*cur
                sgn = 1 if q =='+' else -1
                cur = 0
            if q == '(':
                stack.append(tot)
                stack.append(sgn)
                tot = 0
                sgn = 1
                cur = 0
            if q == ')':
                tot += cur*sgn
                tot = stack.pop()*tot + stack.pop()
                cur = 0
                sgn = 1
        return tot + sgn*cur   

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.calculate, self.calculate2]:
            self.assertEqual(sol("(1+(4+5+2)-3)+(6+8)"), 23)
            self.assertEqual(sol( " 2-1 + 2 "), 3)

if __name__ == "__main__":
    unittest.main()
