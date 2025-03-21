import unittest
from typing import Optional, List
from helpers import *
from collections import Counter

class _ :
    '''
    84: https://leetcode.com/problems/largest-rectangle-in-histogram/description/
    Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
    return the area of the largest rectangle in the histogram.
    '''
    def largestRectangleArea(self, height):
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)): # go through every height
            while height[i] < height[stack[-1]]: # if we reach a height smaller than last encountered, we pop the last one off and check
                last_i = stack.pop()
                h = height[last_i] # n
                before_last_i = stack[-1] # before_last_i holds the index to a height that is bigger than h
                w = i - before_last_i - 1 # -1 because we do not consider the current height
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans  


class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.largestRectangleArea]:
            self.assertEqual(sol([2,1,5,6,2,3]), 10)
            self.assertEqual(sol([2,4]), 4)

if __name__ == "__main__":
    unittest.main()
