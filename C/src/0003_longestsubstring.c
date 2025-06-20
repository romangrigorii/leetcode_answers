// 3: https://leetcode.com/problems/longest-substring-without-repeating-characters/
// Given a string s, find the length of the longest substring without repeating characters.

#include "headers.h"
#include <string.h>

int lengthOfLongestSubstring(char* s) {
    int len = strlen(s);
    if (len == 0) return 0;
    
    int charMap[128]; // ASCII character map
    for (int i = 0; i < 128; i++) {
        charMap[i] = -1;
    }
    
    int maxLength = 0;
    int start = 0;
    
    for (int i = 0; i < len; i++) {
        char c = s[i];
        if (charMap[c] >= start) {
            start = charMap[c] + 1;
        }
        charMap[c] = i;
        maxLength = (i - start + 1 > maxLength) ? i - start + 1 : maxLength;
    }
    
    return maxLength;
} 