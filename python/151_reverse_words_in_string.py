import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    151: https://leetcode.com/problems/reverse-words-in-a-string/
    Given an input string s, reverse the order of the words.

    A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

    Return a string of the words in reverse order concatenated by a single space.

    Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

    Example 1:

    Input: s = "the sky is blue"
    Output: "blue is sky the"
    
    Example 2:

    Input: s = "  hello world  "
    Output: "world hello"
    Explanation: Your reversed string should not contain leading or trailing spaces.
    
    Example 3:

    Input: s = "a good   example"
    Output: "example good a"
    Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
    '''
    def sol1(self, s: str) -> str:
        lst = s.split(" ")[::-1]
        lst2 = []
        for q in lst:
            if q == "" or q == " ":
                pass
            else:
                lst2.append(q)
        return " ".join(lst2)
        
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol("the sky is blue"), "blue is sky the")
            self.assertEqual(sol("  hello world  "), "world hello")

if __name__ == "__main__":
    unittest.main()
