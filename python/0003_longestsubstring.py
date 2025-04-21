import unittest
from typing import Optional, List
from helpers import *

class _ (Helpers):
    '''
    3: https://leetcode.com/problems/longest-substring-without-repeating-characters/
    Given a string s, find the length of the longest substring without repeating characters.    
    '''
    def sol(self, s: str) -> int:
        dict = {}
        length, maxlen = 0, 0
        for i, q in enumerate(s):
            length+=1
            if q in dict:
                length = min(length, i - dict[q])
            maxlen = max(maxlen, length)
            dict[q] = i
        return maxlen

class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        self.assertEqual(self.sol("abcba"), 3)

if __name__ == "__main__":
    unittest.main()

# # #              Big-O analysis
# Time O(N)  : as the function will sweep through every element and add them
# Space O(N) : since we store the numbers in a new LL