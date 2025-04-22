import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    58: https://leetcode.com/problems/length-of-last-word/
    Given a string s consisting of words and spaces, return the length of the last word in the string.

    A word is a maximal substring consisting of non-space characters only.
    '''
    def insert(self, s: str) -> int:
        s_list = s.split(" ")
        s_list = [q for q in s_list if q != ""]
        return len(s_list[-1])
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.insert]:
            self.assertEqual(sol("Hello World"), 5)
            self.assertEqual(sol("   fly me   to   the moon  "), 4)
            self.assertEqual(sol("luffy is still joyboy"), 6)


if __name__ == "__main__":
    unittest.main()
