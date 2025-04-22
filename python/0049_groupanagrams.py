import unittest
from typing import Optional, List
from helpers import *
from collections import Counter
class _ :
    '''
    49: https://leetcode.com/problems/group-anagrams/description/
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
    '''
    def sol1(self, strs: List[str]) -> List[List[str]]:
        d = {}
        out = []
        for q in strs:
            c = Counter(q)
            key = str("".join([a[0] + str(a[1]) for a in  sorted(list(c.items()), key = lambda x: x[0])]))
            d.setdefault(key, []).append(q)
        return list(d.values())

class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        for sol in [self.sol1]:
            self.equal_lists(sol(["eat","tea","tan","ate","nat","bat"]), [["bat"],["nat","tan"],["ate","eat","tea"]])

if __name__ == "__main__":
    unittest.main()
