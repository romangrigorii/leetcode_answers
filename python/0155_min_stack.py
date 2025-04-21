import unittest
from typing import Optional, List
from helpers import *

class MinStack(Helpers) :
    '''
    155: https://leetcode.com/problems/min-stack/description/
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.
    You must implement a solution with O(1) time complexity for each function.
    '''

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack: min_val = val
        else: min_val = min(val, self.stack[-1][1])
        self.stack.append((val, min_val))

    def pop(self) -> None:
        self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1] 


def func1():
    res = []
    q = MinStack()
    res.append(q.push(-2))
    res.append(q.push(0))
    res.append(q.push(-3))
    res.append(q.getMin())
    res.append(q.pop())
    res.append(q.top())
    res.append(q.getMin())
    return res
            
class test(unittest.TestCase, MinStack, Helpers):
    def test_(self):    
        self.assertEqual(func1(), [None,None,None,-3,None,0,-2])

if __name__ == "__main__":
    unittest.main()
