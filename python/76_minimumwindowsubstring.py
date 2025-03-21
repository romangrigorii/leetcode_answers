import unittest
from typing import Optional, List
from helpers import *
from collections import Counter

class _ :
    '''
    76: https://leetcode.com/problems/minimum-window-substring/description/
    Given two strings s and t of lengths m and n respectively, return the minimum window substring
    of s such that every character in t (including duplicates) is included in the window. 
    If there is no such substring, return the empty string "". 
    The testcases will be generated such that the answer is unique.
    '''
    def minWindow(self, s: str, t: str) -> str:  # this approach hit TLE on leetcode
        shortest = []
        t = Counter(t)
        to = t.copy()
        def minWindowHelper(s,t, current, best):        
            if sum(t.values()) == 0:
                if not best:
                    best.append((current, len(current)))
                elif len(current) < best[0][1]:
                    best[0] = (current, len(current))
                return
            if not s: return
            if s[0] in t and t[s[0]]>0:
                t[s[0]]-=1
                minWindowHelper(s[1:], t, current+s[0], best)
                t[s[0]]+=1
            minWindowHelper(s[1:], t, current+s[0], best) # continue on
            if t == to:
                minWindowHelper(s[1:], t, current, best) # continue on

        minWindowHelper(s, t, '', shortest)
        return "".join(shortest[0][0]) if shortest else ''
    
    def minWindow2(self, s: str, t: str) -> str:  
        need, missing = Counter(t), len(t) # need keeps track of which characters we still need, missing keeps track of how many
        l = L = R = 0
        for r in range(len(s)): # j keeps track of right position 
            missing -= need[s[r]] > 0 # missing hold the number of elements we still need
            need[s[r]] -= 1
            if not missing: # once we are not missing then we are just tightening the left 
                while l < r + 1 and need[s[l]] < 0: # add characters back one by one starting from the leftmost point
                    need[s[l]] += 1
                    l += 1
                if not R or r + 1 - l <= R - L: # we record the left point and keep going
                    L, R = l, r + 1
        return s[L:R]
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.minWindow, self.minWindow2]:
            self.assertEqual(sol("ADOBECODEBANC","ABC"),"BANC")

if __name__ == "__main__":
    unittest.main()
