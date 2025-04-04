# # # 
# Given a string s, how many unique substrings of s are palindromes?
# Read the same formward and backward
# return an int. Example:
# mokkori: m o k r i kk okko
# Answer: 7

import sys
sys.path.insert(0, "../..")

import unittest
from typing import Optional, List
from helpers import *
import numpy as np
class _ (Helpers):    
    def sol1(self, s):
        L = len(s)

        palindromes = set()

        def walk(idxL, idxR):
            if s[idxL]==s[idxR]: palindromes.add(s[idxL:idxR+1])
            while idxL-1>0 and idxR+1<L and s[idxL-1]==s[idxR+1]: 
                idxL-=1
                idxR+=1
                palindromes.add(s[idxL:idxR+1])
        
        for i, q in enumerate(s):
            walk(i,i)
            if i+1<L: walk(i,i+1)
        
        return len(palindromes)

    def sol2(self, s):
        '''
        We want to go through the array and append the list of new generated substrings
        '''
        palindromes = set()
        def go_through(st,en,s):
            while st>=0 and en<len(s) and s[st]==s[en]:
                palindromes.add(s[st:en+1])
                st-=1
                en+=1
        for i in range(len(s)):
            go_through(i,i,s)
            go_through(i,i+1,s)
        return len(palindromes)

class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        for sol in [self.sol1, self.sol2]:
            self.assertEqual(sol('mokkori'), 7)
            self.assertEqual(sol(''), 0)
            self.assertEqual(sol('abaaba'), 6) # a, b, aba, aa, baab, abaaba
            

unittest.main()