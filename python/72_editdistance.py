import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    72: https://leetcode.com/problems/edit-distance/description/
    Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
    You have the following three operations permitted on a word:
    Insert a character
    Delete a character
    Replace a character
    '''
    def minDistance(self, word1: str, word2: str) -> int:
        w1 = len(word1)
        w2 = len(word2)
        op = [[0]*w2 for i in range(w1)]
        def helper(p1, p2):
            if p1 == w1: return w2 - p2 # return the rest of conversion
            if p2 == w2: return w1 - p1 # return the rest of conversion
            if op[p1][p2] == 0:
                if word1[p1] == word2[p2]: 
                    return helper(p1+1,p2+1)
                res1 = helper(p1+1,p2)
                res2 = helper(p1,p2+1)
                res3 = helper(p1+1,p2+1)
                op[p1][p2] = 1 + min(res1, res2, res3)
            return op[p1][p2]
        return helper(0,0)

class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.minDistance]:
            self.assertEqual(sol("horse", "ros"), 3)

if __name__ == "__main__":
    unittest.main()
