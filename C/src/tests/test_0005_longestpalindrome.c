#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include "../headers.h"

void test_1_longest_palindrome() {
    // Test case: "babad" -> "aba"
    char* s = "babad";
    char* result = longestPalindrome(s);
    assert(strcmp(result, "aba") == 0);
    printf("Testing: test_1_longest_palindrome: Success\n");
    free(result);
}

void test_2_longest_palindrome() {
    // Test case: "cbbd" -> "bb"
    char* s = "cbbd";
    char* result = longestPalindrome(s);
    assert(strcmp(result, "bb") == 0);
    printf("Testing: test_2_longest_palindrome: Success\n");
    free(result);
}

void test_3_longest_palindrome() {
    // Test case: "a" -> "a"
    char* s = "a";
    char* result = longestPalindrome(s);
    assert(strcmp(result, "a") == 0);
    printf("Testing: test_3_longest_palindrome: Success\n");
    free(result);
}

void test_4_longest_palindrome() {
    // Test case: "ac" -> "a"
    char* s = "ac";
    char* result = longestPalindrome(s);
    assert(strcmp(result, "a") == 0 || strcmp(result, "c") == 0);
    printf("Testing: test_4_longest_palindrome: Success\n");
    free(result);
}

void test_5_longest_palindrome() {
    // Test case: "racecar" -> "racecar"
    char* s = "racecar";
    char* result = longestPalindrome(s);
    assert(strcmp(result, "racecar") == 0);
    printf("Testing: test_5_longest_palindrome: Success\n");
    free(result);
}

void run_longest_palindrome_tests() {
    printf("Running Longest Palindrome Tests...\n");
    test_1_longest_palindrome();
    test_2_longest_palindrome();
    test_3_longest_palindrome();
    test_4_longest_palindrome();
    test_5_longest_palindrome();
    printf("All Longest Palindrome tests completed successfully!\n\n");
} 