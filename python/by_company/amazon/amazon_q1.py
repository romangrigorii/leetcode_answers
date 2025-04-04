import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    This is an amazon question
    '''
    def sol1(self, s, arr):
        left = [0]*len(s)
        right = [0]*len(s)
        hitwall, sofar, sofar_ = 0, 0, 0
        for i in range(len(s)):
            if s[i] == '|':
                sofar_ = sofar
                if hitwall == 0:
                    hitwall = 1
            else:
                sofar += hitwall
            left[i] = sofar_
        hitwall, sofar, sofar_ = 0, 0, 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == '|':
                sofar_ = sofar
                if hitwall == 0:
                    hitwall = 1
            else:
                sofar += hitwall
            right[i] = sofar_    
        
        print(left)
        print(right)
        out = []
        for q in arr:
            out.append(min(left[q[1]-1] - left[q[0]-1], right[q[0]-1] - right[q[1]-1]))
        print(out)
    
    def sol2(self, s, arr):
        left = [0]*len(s)
        right = [0]*len(s)
        idx = []
        for i in range(len(s)):
            if s[i] == '|': idx.append(i)
        idx = [0] + idx + [len(s)-1]
        q = 1
        for i in range(len(s)):
            if i == idx[q]: 
                q += 1
            left[i] = idx[q-1] - q + 1
        q = len(idx)-1
        for i in range(len(idx)-1,-1,-1):
            if i == idx[q]: q -= 1
            right[i] = idx[q] - q - idx[-1]
        print(left)
        print(right)

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol('**|*|****|*', [[1,5],[1,6],[4,8],[5,10],[5,11]]), [1,1,0,4,4])

if __name__ == "__main__":
    unittest.main()
