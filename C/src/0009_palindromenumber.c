// 9: https://leetcode.com/problems/palindrome-number/
// Given an integer x, return true if x is a palindrome, and false otherwise.

#include "headers.h"

int isPalindrome(int x) {
    // Negative numbers are not palindromes
    if (x < 0) {
        return 0;
    }
    
    // Single digit numbers are palindromes
    if (x < 10) {
        return 1;
    }
    
    // Find the number of digits
    int original = x;
    int reversed = 0;
    
    while (x > 0) {
        int digit = x % 10;
        reversed = reversed * 10 + digit;
        x /= 10;
    }
    
    return original == reversed;
} 