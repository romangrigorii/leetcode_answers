// 6: https://leetcode.com/problems/zigzag-conversion/
// The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
// P   A   H   N
// A P L S I I G
// Y   I   R
// And then read line by line: "PAHNAPLSIIGYIR"

#include "headers.h"
#include <string.h>
#include <stdlib.h>

char* convert(char* s, int numRows) {
    int len = strlen(s);
    if (numRows == 1 || len <= numRows) {
        char* result = (char*)malloc(len + 1);
        strcpy(result, s);
        return result;
    }
    
    // Allocate memory for result
    char* result = (char*)malloc(len + 1);
    int resultIndex = 0;
    
    // Process each row
    for (int row = 0; row < numRows; row++) {
        int step1 = (numRows - 1 - row) * 2;
        int step2 = row * 2;
        
        int index = row;
        while (index < len) {
            result[resultIndex++] = s[index];
            
            // Add character from step1 if it's not the last row
            if (step1 > 0 && index + step1 < len) {
                result[resultIndex++] = s[index + step1];
            }
            
            // Move to next position
            index += step1 + step2;
            
            // If both steps are 0, move by 1
            if (step1 == 0 && step2 == 0) {
                index++;
            }
        }
    }
    
    result[resultIndex] = '\0';
    return result;
} 