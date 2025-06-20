// 7: https://leetcode.com/problems/reverse-integer/
// Given a signed 32-bit integer x, return x with its digits reversed.
// If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

#include "headers.h"
#include <limits.h>

int reverse(int x) {
    int result = 0;
    
    while (x != 0) {
        int digit = x % 10;
        
        // Check for overflow before multiplying
        if (result > INT_MAX / 10 || (result == INT_MAX / 10 && digit > 7)) {
            return 0;
        }
        if (result < INT_MIN / 10 || (result == INT_MIN / 10 && digit < -8)) {
            return 0;
        }
        
        result = result * 10 + digit;
        x /= 10;
    }
    
    return result;
} 