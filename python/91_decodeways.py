import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    91: https://leetcode.com/problems/decode-ways/
    A message containing letters from A-Z can be encoded into numbers using the following mapping:
    'A' -> "1"
    'B' -> "2"
    ...
    'Z' -> "26"
    To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the 
    mapping above (there may be multiple ways). For example, "11106" can be mapped into:
    "AAJF" with the grouping (1 1 10 6)
    "KJF" with the grouping (11 10 6)
    Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

    Given a string s containing only digits, return the number of ways to decode it.

    The test cases are generated so that the answer fits in a 32-bit integer.

 
    '''
    def numDecodings(self, s: str) -> int:
        dp = [0] + [1] + [0]*len(s)
        for i in range(len(s)):
            d = int(s[i])<=6 and i > 0 and (s[i-1] == '1' or s[i-1] == '2')
            h = int(s[i])>0
            dp[i+2] = dp[i+1]*h + d*dp[i]
        return dp[-1]
    
    def numDecodings2(self, s: str) -> int:
        s = [int(q) for q in s]
        num_out = [0] + [1]*(len(s)+1) # index 1 corresponds to being able to decode with the digit value
        for q in range(len(s)):
            num_out[q+2] = num_out[q+1]*(s[q]>0)
            num_out[q+2] += num_out[q]*(s[q-1] == 1 or (s[q-1] == 2 and s[q]<=6))
        return num_out[-1]
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.numDecodings, self.numDecodings2]:
            self.assertEqual(sol("12"), 2)
            self.assertEqual(sol("226"), 3)
            self.assertEqual(sol("06"), 0)
            self.assertEqual(sol("11234"), 5)
if __name__ == "__main__":
    unittest.main()
