import unittest
from typing import Optional, List
from helpers import *
from collections import Counter

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
        Optimized sliding window approach that checks all possible starting positions
        '''
        if not s or not words or not words[0]: 
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        s_len = len(s)
        
        # Use Counter for efficient word counting
        word_count = Counter(words)
        result = []
        
        # Check all possible starting positions (not just multiples of word_len)
        for start in range(word_len):
            # Use sliding window for this starting position
            left = start
            current_count = Counter()
            word_used = 0
            
            for right in range(start, s_len - word_len + 1, word_len):
                current_word = s[right:right + word_len]
                
                # If word is not in our target words, reset window
                if current_word not in word_count:
                    left = right + word_len
                    current_count.clear()
                    word_used = 0
                    continue
                
                current_count[current_word] += 1
                word_used += 1
                
                # If we have too many of this word, shrink window from left
                while current_count[current_word] > word_count[current_word]:
                    left_word = s[left:left + word_len]
                    current_count[left_word] -= 1
                    word_used -= 1
                    left += word_len
                
                # If we have exactly the right number of words, check if it's a valid substring
                if word_used == num_words:
                    result.append(left)
                    # Move left pointer to continue searching
                    left_word = s[left:left + word_len]
                    current_count[left_word] -= 1
                    word_used -= 1
                    left += word_len
        
        return result
    
    def findSubstringBruteForce(self, s: str, words: List[str]) -> List[int]:
        """
        Brute force approach - checks every possible starting position
        Less efficient but easier to understand
        """
        if not s or not words or not words[0]:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        s_len = len(s)
        
        # Create word frequency map
        word_count = Counter(words)
        result = []
        
        # Check every possible starting position
        for i in range(s_len - total_len + 1):
            # Check if substring starting at i is valid
            current_count = Counter()
            valid = True
            
            for j in range(num_words):
                word = s[i + j * word_len:i + (j + 1) * word_len]
                if word not in word_count:
                    valid = False
                    break
                
                current_count[word] += 1
                if current_count[word] > word_count[word]:
                    valid = False
                    break
            
            if valid:
                result.append(i)
        
        return result
    

class test(unittest.TestCase, _ , Helpers):
    def test_all_solutions(self):
        # Define all test cases with input and expected output
        test_cases = [
            # Basic cases
            ("barfoothefoobarman", ["foo","bar"], [0,9]),
            ("wordgoodgoodgoodbestword", ["word","good","best","word"], []),
            
            # Edge cases
            ("", ["foo","bar"], []),                    # Empty string
            ("barfoothefoobarman", [], []),             # Empty words array
            ("barfoothefoobarman", [""], []),           # Empty word
            
            # Single word cases
            ("foobar", ["foo"], [0]),                   # Single word match
            ("foobar", ["bar"], [3]),                   # Single word match at end
            ("foobar", ["baz"], []),                    # Single word no match
            
            # Multiple words cases
            ("foobarbaz", ["foo","bar"], [0]),          # Two words consecutive
            ("foobarbaz", ["bar","baz"], [3]),          # Two words at end
            ("foobarbaz", ["foo","baz"], []),           # Two words not consecutive
            
            # Duplicate words
            ("foofoo", ["foo","foo"], [0]),             # Duplicate words match
            ("foobarfoo", ["foo","bar","foo"], [0]),    # Duplicate words in sequence
            ("foobarfoo", ["foo","foo","bar"], [0]),    # Duplicate words different order
            
            # Complex cases
            ("barfoofoobarthefoobarman", ["bar","foo","the"], [6,9,12]),
            ("wordgoodgoodgoodbestword", ["word","good","best","good"], [8]),
            ("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"], [13]),
            
            # No matches
            ("foobar", ["foo","baz"], []),              # One word doesn't exist
            ("foobar", ["foo","bar","baz"], []),        # Extra word
            ("foobar", ["foo"], [0]),                   # Single word match (not missing)
            
            # Overlapping cases - need exact word count, not overlapping
            ("aaaa", ["aa","aa"], [0]),                 # Two "aa" words starting at 0
            ("aaaa", ["aa"], [0,1,2]),                  # Single "aa" word at positions 0, 1, and 2 (overlapping)
            
            # Very short cases
            ("a", ["a"], [0]),                          # Single character
            ("ab", ["a","b"], [0]),                     # Two characters
            ("ab", ["ab"], [0]),                        # Two characters as one word
            
            # Long word cases - need exact matches, not overlapping
            ("abcdefghijklmnop", ["abcd","efgh"], [0]),  # Two long words at start
            ("abcdefghijklmnop", ["abcd","efgh","ijkl"], [0]),  # Three long words at start
        ]
        
        # Test all solutions with the same test cases
        for s, words, expected in test_cases:
            with self.subTest(s=s, words=words, expected=expected):
                # Test the optimized sliding window solution
                result1 = self.findSubstring(s, words)
                self.assertEqual(sorted(result1), sorted(expected), 
                                f"findSubstring failed for s='{s}', words={words}")
                
                # Test the brute force solution
                result2 = self.findSubstringBruteForce(s, words)
                self.assertEqual(sorted(result2), sorted(expected), 
                                f"findSubstringBruteForce failed for s='{s}', words={words}")
    

if __name__ == "__main__":
    unittest.main()
