#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "../headers.h"

void test_1_longest_substring() {
    // Test case: "abcabcbb" -> 3
    char* s = "abcabcbb";
    int result = lengthOfLongestSubstring(s);
    assert(result == 3);
    printf("Testing: test_1_longest_substring: Success\n");
}

void test_2_longest_substring() {
    // Test case: "bbbbb" -> 1
    char* s = "bbbbb";
    int result = lengthOfLongestSubstring(s);
    assert(result == 1);
    printf("Testing: test_2_longest_substring: Success\n");
}

void test_3_longest_substring() {
    // Test case: "pwwkew" -> 3
    char* s = "pwwkew";
    int result = lengthOfLongestSubstring(s);
    assert(result == 3);
    printf("Testing: test_3_longest_substring: Success\n");
}

void test_4_longest_substring() {
    // Test case: "" -> 0
    char* s = "";
    int result = lengthOfLongestSubstring(s);
    assert(result == 0);
    printf("Testing: test_4_longest_substring: Success\n");
}

void test_5_longest_substring() {
    // Test case: "abcba" -> 3
    char* s = "abcba";
    int result = lengthOfLongestSubstring(s);
    assert(result == 3);
    printf("Testing: test_5_longest_substring: Success\n");
}

void run_longest_substring_tests() {
    printf("Running Longest Substring Tests...\n");
    test_1_longest_substring();
    test_2_longest_substring();
    test_3_longest_substring();
    test_4_longest_substring();
    test_5_longest_substring();
    printf("All Longest Substring tests completed successfully!\n\n");
} 