import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    174: https://leetcode.com/problems/dungeon-game/description/

    The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
    For example, "ACGAATTCCG" is a DNA sequence.
    When studying DNA, it is useful to identify repeated sequences within the DNA.

    Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.
    '''
    def sol1(self, s: str) -> List[str]:
        m = {}
        for i in range(len(s)-10+1):
            m[s[i:i+10]] = m.get(s[i:i+10], 0) + 1
        return [q[0] for q in m.items() if q[1]>1]
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"), ["AAAAACCCCC","CCCCCAAAAA"])
            self.assertEqual(sol("AAAAAAAAAAAAA"), ["AAAAAAAAAA"])

if __name__ == "__main__":
    unittest.main()
