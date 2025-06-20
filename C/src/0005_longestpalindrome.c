// 5: https://leetcode.com/problems/longest-palindromic-substring/
// Given a string s, return the longest palindromic substring in s.

#include "headers.h"
#include <string.h>
#include <stdlib.h>

// Helper function to expand around center
void expandAroundCenter(char* s, int left, int right, int* start, int* maxLen) {
    int len = strlen(s);
    while (left >= 0 && right < len && s[left] == s[right]) {
        left--;
        right++;
    }
    
    int currentLen = right - left - 1;
    if (currentLen > *maxLen) {
        *start = left + 1;
        *maxLen = currentLen;
    }
}

char* longestPalindrome(char* s) {
    int len = strlen(s);
    if (len <= 1) {
        char* result = (char*)malloc(len + 1);
        strcpy(result, s);
        return result;
    }
    
    int start = 0;
    int maxLen = 1;
    
    // Check each character as center
    for (int i = 0; i < len; i++) {
        // Odd length palindrome
        expandAroundCenter(s, i, i, &start, &maxLen);
        // Even length palindrome
        expandAroundCenter(s, i, i + 1, &start, &maxLen);
    }
    
    // Create result string
    char* result = (char*)malloc(maxLen + 1);
    strncpy(result, s + start, maxLen);
    result[maxLen] = '\0';
    
    return result;
} 