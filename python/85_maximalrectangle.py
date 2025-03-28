import unittest
from typing import Optional, List
from helpers import *
from collections import Counter

class _ :
    '''
    85: https://leetcode.com/problems/maximal-rectangle/description/
    Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area. 
    '''
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n + 1)
        ans = 0
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w)
                stack.append(i)
        return ans

class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.maximalRectangle]:
            self.assertEqual(sol([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]), 6)
            self.assertEqual(sol([["0"]]), 0)
            self.assertEqual(sol([["1"]]), 1)

if __name__ == "__main__":
    unittest.main()
