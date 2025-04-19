import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    1573: https://leetcode.com/problems/number-of-ways-to-split-a-string/
    Given a binary string s, you can split s into 3 non-empty strings s1, s2, and s3 where s1 + s2 + s3 = s.
    Return the number of ways s can be split such that the number of ones is the same in s1, s2, and s3. Since the answer may be too large, return it modulo 109 + 7.
    '''
    def numWays(self, s: str) -> int:
        mod = 10**9 + 7
        n = len(s)
        ones_count = s.count('1')
        # If ones can't be split into three equal groups, return 0.
        if ones_count % 3 != 0:
            return 0
        # If there are no ones, choose two random split points from n - 1 positions.
        if ones_count == 0:
            return ((n - 1) * (n - 2) // 2) % mod

        ones_per_split = ones_count // 3
        first_split_ways = 0
        second_split_ways = 0
        ones_count_through_splits = 0
        # Traverse chars in str
        for c in s:
            if c == '1':
                ones_count_through_splits += 1
            # Count ways to place first split
            if ones_count_through_splits == ones_per_split:
                first_split_ways += 1
            # Count ways to place second split
            elif ones_count_through_splits == 2 * ones_per_split:
                second_split_ways += 1

        # Return number of ways for placing both splits.
        return (first_split_ways * second_split_ways) % mod 

class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.numWays]:
            self.assertEqual(sol("0000"),3)
            self.assertEqual(sol("1001"),0)
            self.assertEqual(sol("10101"),4)

if __name__ == "__main__":
    unittest.main()
