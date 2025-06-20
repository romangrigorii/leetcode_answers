#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "../headers.h"

void test_1_regular_expression_matching() {
    // Test case: "aa", "a" -> false
    int result = isMatch("aa", "a");
    assert(result == 0);
    printf("Testing: test_1_regular_expression_matching: Success\n");
}

void test_2_regular_expression_matching() {
    // Test case: "aa", "a*" -> true
    int result = isMatch("aa", "a*");
    assert(result == 1);
    printf("Testing: test_2_regular_expression_matching: Success\n");
}

void test_3_regular_expression_matching() {
    // Test case: "ab", ".*" -> true
    int result = isMatch("ab", ".*");
    assert(result == 1);
    printf("Testing: test_3_regular_expression_matching: Success\n");
}

void test_4_regular_expression_matching() {
    // Test case: "mississippi", "mis*is*p*." -> false
    int result = isMatch("mississippi", "mis*is*p*.");
    assert(result == 0);
    printf("Testing: test_4_regular_expression_matching: Success\n");
}

void run_regular_expression_matching_tests() {
    printf("Running Regular Expression Matching Tests...\n");
    test_1_regular_expression_matching();
    test_2_regular_expression_matching();
    test_3_regular_expression_matching();
    test_4_regular_expression_matching();
    printf("All Regular Expression Matching tests completed successfully!\n\n");
} 