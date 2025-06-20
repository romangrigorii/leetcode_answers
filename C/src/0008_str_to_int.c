// 8: https://leetcode.com/problems/string-to-integer-atoi/
// Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

#include "headers.h"
#include <ctype.h>
#include <limits.h>

int myAtoi(char* s) {
    // Skip leading whitespace
    while (*s == ' ') {
        s++;
    }
    
    if (*s == '\0') {
        return 0;
    }
    
    // Handle sign
    int sign = 1;
    if (*s == '-' || *s == '+') {
        sign = (*s == '-') ? -1 : 1;
        s++;
    }
    
    // Convert digits
    long long result = 0;
    while (*s >= '0' && *s <= '9') {
        result = result * 10 + (*s - '0');
        
        // Check for overflow
        if (sign * result > INT_MAX) {
            return INT_MAX;
        }
        if (sign * result < INT_MIN) {
            return INT_MIN;
        }
        
        s++;
    }
    
    return (int)(sign * result);
} 