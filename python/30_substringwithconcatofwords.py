import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    30: https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
    You are given a string s and an array of strings words. All the strings of words are of the same length.
    A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.
    For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are
    all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any
    permutation of words.
    Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.
    '''
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        '''
        Go through every letter in str and remove words from the dictionary as they appear
        '''
        if not s or not words or not words[0]: return []
        word_dict = {}
        for word in words:
            word_dict.setdefault(word, 0)
            word_dict[word]+=1

        L = len(s)
        W = len(words)
        wL = len(words[0])

        def contains_all(st):
            wd = word_dict.copy()
            for i in range(W):
                if wd.get(s[st+i*wL:st+(i+1)*wL], 0):
                    wd[s[st+i*wL:st+(i+1)*wL]] -=1
                else:
                    return False
            return True
        
        return [s for s in range(L-W*wL+1) if contains_all(s)]
    

class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        self.assertEqual(self.findSubstring("barfoothefoobarman", ["foo","bar"]), [0,9])
        self.assertEqual(self.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]), [])


if __name__ == "__main__":
    unittest.main()
