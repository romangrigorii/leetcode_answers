import unittest
from typing import Optional, List
from helpers import *

class _ (Helpers):
    '''
    17: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
    Return the answer in any order.
    A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
    '''
    def sol1(self, digits: str) -> List[str]:
        ma = {1: "", 2: "abc", 3 : "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8 : "tuv", 9: "wxyz"}
        out = []
        for q in digits:
            outn = []
            for o in (out if out else [""]):
                outn.extend(o + z for z in ma[int(q)])
            out = outn
        return out
    
class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        self.assertEqual(self.sol1(digits = "23"), ["ad","ae","af","bd","be","bf","cd","ce","cf"])
        self.assertEqual(self.sol1(digits = ""), [])
        self.assertEqual(self.sol1(digits = "2"), ["a","b","c"])


if __name__ == "__main__":
    unittest.main()