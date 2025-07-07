import unittest
from typing import Optional, List
from helpers import *

class _ (ListNode):
    '''
    32: https://leetcode.com/problems/longest-valid-parentheses/description/
    Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) 
    parentheses substring
    '''
    
    def longestValidParentheses(self, s: str) -> int:
        """
        Find the length of the longest valid parentheses substring.
        
        Algorithm: Two-pass approach
        1. Left to right pass: Count '(' and ')', reset when invalid
        2. Right to left pass: Count '(' and ')', reset when invalid
        3. Take the maximum from both passes
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(s)
        max_len = 0
        
        # Pass 1: Left to right
        left_count = right_count = 0
        for i in range(n):
            if s[i] == '(':

                
                left_count += 1
            else:
                right_count += 1
            
            # If we have equal counts, we have a valid substring
            if left_count == right_count:
                max_len = max(max_len, 2 * left_count)
            # If right count exceeds left count, reset (invalid)
            elif right_count > left_count:
                left_count = right_count = 0
        
        # Pass 2: Right to left
        left_count = right_count = 0
        for i in range(n - 1, -1, -1):
            if s[i] == '(':
                left_count += 1
            else:
                right_count += 1
            
            # If we have equal counts, we have a valid substring
            if left_count == right_count:
                max_len = max(max_len, 2 * left_count)
            # If left count exceeds right count, reset (invalid)
            elif left_count > right_count:
                left_count = right_count = 0
        
        return max_len
    
    def longestValidParenthesesStack(self, s: str) -> int:
        """
        Stack-based solution - more intuitive but uses O(n) space.
        
        Algorithm:
        1. Use a stack to keep track of indices
        2. Push -1 as initial base case
        3. For each '(' push its index
        4. For each ')' pop and calculate length
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = [-1]  # Base case: empty stack
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:  # Stack is empty
                    stack.append(i)  # New base case
                else:
                    max_len = max(max_len, i - stack[-1])
        
        return max_len
    
    def longestValidParenthesesStackAndDP(self, s: str) -> int:
        dp, stack = [0]*(1+len(s)), []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i) # the last time '(' was encountered
            else:
                if stack:
                    last = stack.pop()
                    dp[i+1] = dp[last] + i - last + 1
        return max(dp) 
       
 
class test(unittest.TestCase, _, ListNode):
    def test_all_solutions(self):
        # Define all test cases
        test_cases = [
            ('(()()', 4),         # Basic case
            (')()())', 4),        # Multiple valid substrings
            ('', 0),              # Empty string
            ('(', 0),             # Single opening parenthesis
            (')', 0),             # Single closing parenthesis
            ('()', 2),            # Simple valid pair
            ('(())', 4),          # Nested valid parentheses
            ('()()', 4),          # Consecutive valid pairs
            ('(()())', 6),        # Complex valid substring
            (')()()(', 4),        # Edge case with leading/trailing invalid
            ('((((()))))', 10),   # Very long valid substring
            ('((()', 2),          # Partial valid substring
            (')))(', 0),          # No valid substring
            ('()(()', 2),         # Valid substring at beginning
            ('(()(((()', 2),      # Complex case with multiple invalid parts
        ]
        
        # Test all solutions with the same test cases
        for s, expected in test_cases:
            with self.subTest(s=s, expected=expected):
                # Test the two-pass solution
                result1 = self.longestValidParentheses(s)
                self.assertEqual(result1, expected, f"Two-pass solution failed for '{s}'")
                
                # Test the stack solution
                result2 = self.longestValidParenthesesStack(s)
                self.assertEqual(result2, expected, f"Stack solution failed for '{s}'")
                
                # Test the original Stack + DP solution
                result3 = self.longestValidParenthesesStackAndDP(s)
                self.assertEqual(result3, expected, f"DP solution failed for '{s}'")

if __name__ == "__main__":
    unittest.main()