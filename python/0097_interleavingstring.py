import unittest
from typing import Optional, List
from helpers import *
from functools import lru_cache 

class _(Helpers) :
    '''
    97: https://leetcode.com/problems/interleaving-string/
    Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
    An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that: 
    s = s1 + s2 + ... + sn
    t = t1 + t2 + ... + tm
    |n - m| <= 1
    The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
    Note: a + b is the concatenation of strings a and b.
    '''
    def sol1(self, s1: str, s2: str, s3: str) -> bool:
        L1, L2, L3 = len(s1), len(s2), len(s3)
        if L1+L2 != L3: return False
        if not s1: return s2 == s3
        if not s2: return s1 == s3
        dp = [[False]*(1+L2) for i in range(1+L1)]
        dp[0] = [True]*(1+L2)
        for i in range(1+L1):
            dp[i][0] = True
        def helper(p1,p2,p3):
            if p3==L3 and p1==L1 and p2==L2: 
                dp[-1][-1] = True
            else:
                if dp[p1][p2] and p1<L1 and s1[p1] == s3[p3]: 
                    dp[p1+1][p2] = True
                    helper(p1+1,p2,p3+1)
                if dp[p1][p2] and p2<L2 and s2[p2] == s3[p3]: 
                    dp[p1][p2+1] = True
                    helper(p1,p2+1,p3+1)
        helper(0,0,0)
        return dp[-1][-1]
    
    def sol2(self, s1, s2, s3):
        @lru_cache(None)
        def dp(i, j):
            if i == -1 and j == -1: return True
            return (j >= 0 and s2[j] == s3[i+j+1] and dp(i, j-1)) or (i >= 0 and s1[i] == s3[i+j+1] and dp(i-1,j))
        
        return len(s1) + len(s2) == len(s3) and dp(len(s1) - 1, len(s2) - 1)
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1, self.sol2]:
            self.assertEqual(sol(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"), True)
            self.assertEqual(sol(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"), False)
            self.assertEqual(sol(s1 = "a", s2 = "", s3 = "a"), True)
            self.assertEqual(sol(s1 = "aabaac", s2 = "aadaaeaaf", s3 = "aadaaeaabaafaac"), True)

if __name__ == "__main__":   
    unittest.main()
