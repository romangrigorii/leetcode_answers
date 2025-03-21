import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    1143: https://leetcode.com/problems/longest-common-subsequence/
    '''
    def sol1(self, text1: str, text2: str) -> int:
        '''
        The idea is to traverse each of the arrays and create a 2x2 matrix of elements which
        have been present in both thus far. We expand the arrays to be larger by1 for 
        simplicity. 
        '''
        L1 = len(text1)
        L2 = len(text2)
        q = [[0]*(L2+1)]
        for i in range (1,L1+1):
            q.append(q[-1].copy())
        for i in range(1,L1+1):
            for j in range(1,L2+1):
                q[i][j] = q[i-1][j-1]+1 if text1[i-1] == text2[j-1] else max(q[i-1][j], q[i][j-1])
        return q[L1][L2]


class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol("abcde", "ace"), 3)

if __name__ == "__main__":
    unittest.main()
