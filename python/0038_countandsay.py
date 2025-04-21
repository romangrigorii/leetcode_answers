import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    38: https://leetcode.com/problems/count-and-say/description/
    The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
    countAndSay(1) = "1"
    countAndSay(n) is the run-length encoding of countAndSay(n - 1).
    Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical 
    characters (repeated 2 or more times) with the concatenation of the character and the number marking the 
    count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", 
    replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".
    Given a positive integer n, return the nth element of the count-and-say sequence.
    '''
    def specialCounter(self, s):
        s += ' '
        string = ''
        i, j = 1, 0
        while(j<len(s)-1):
            if s[j] == s[j+1]: i+=1
            else:
                string += str(i) + s[j] # a counter of sorts -> only counts same values grouped together
                i = 1                
            j+=1
        return string

    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        string = self.countAndSay(n-1)
        return self.specialCounter(string)
    

class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        self.assertEqual(self.countAndSay(5), "111221")
        self.assertEqual(self.countAndSay(1), '1')

if __name__ == "__main__":
    unittest.main()
