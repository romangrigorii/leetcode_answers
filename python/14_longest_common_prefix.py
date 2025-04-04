import unittest
from typing import Optional, List
from helpers import *

class _ (Helpers):
    '''
    14: https://leetcode.com/problems/longest-common-prefix/
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".
    '''
    def sol1(self, strs: List[str]) -> str:
        '''
        The reasoning behind this solution is that we start with the first word in the list,
        and then trim to have the starting characters match the starting charatcers of the following word.
        Those starting chratacters than propagate to the next word, and so on, each time being trimmed. 
        '''
        if not strs: return ""
        lc = strs[0]
        for i in range(1,len(strs)):            
            nw = strs[i] # new word
            if not nw or not lc: return ""
            lcL = len(lc)
            nwL = len(nw)
            jj = 0
            while jj < nwL and jj < lcL and nw[jj] == lc[jj]:
                jj+=1
            lc = lc[:jj]
            if not lc: return ""
        return lc
    
    
class test(unittest.TestCase, _ , Helpers):
    def test_1(self):
        self.assertEqual(self.sol1(["flower","flow","flight"]), "fl")
        self.assertEqual(self.sol1(["dog","racecar","car"]), "")

if __name__ == "__main__":
    unittest.main()