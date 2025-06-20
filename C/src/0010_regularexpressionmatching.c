// 10: https://leetcode.com/problems/regular-expression-matching/
// Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*'

#include "headers.h"
#include <string.h>

// Dynamic programming solution
int isMatch(char* s, char* p) {
    int sLen = strlen(s);
    int pLen = strlen(p);
    
    // Create DP table
    int** dp = (int**)malloc((sLen + 1) * sizeof(int*));
    for (int i = 0; i <= sLen; i++) {
        dp[i] = (int*)calloc(pLen + 1, sizeof(int));
    }
    
    // Base case: empty pattern matches empty string
    dp[0][0] = 1;
    
    // Handle patterns with *
    for (int j = 1; j <= pLen; j++) {
        if (p[j-1] == '*') {
            dp[0][j] = dp[0][j-2];
        }
    }
    
    // Fill DP table
    for (int i = 1; i <= sLen; i++) {
        for (int j = 1; j <= pLen; j++) {
            if (p[j-1] == '.' || p[j-1] == s[i-1]) {
                dp[i][j] = dp[i-1][j-1];
            } else if (p[j-1] == '*') {
                dp[i][j] = dp[i][j-2]; // Match 0 occurrences
                if (p[j-2] == '.' || p[j-2] == s[i-1]) {
                    dp[i][j] = dp[i][j] || dp[i-1][j]; // Match 1 or more occurrences
                }
            }
        }
    }
    
    int result = dp[sLen][pLen];
    
    // Free memory
    for (int i = 0; i <= sLen; i++) {
        free(dp[i]);
    }
    free(dp);
    
    return result;
} 