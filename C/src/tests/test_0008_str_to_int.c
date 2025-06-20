#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "../headers.h"

void test_1_string_to_integer() {
    // Test case: "42" -> 42
    int result = myAtoi("42");
    assert(result == 42);
    printf("Testing: test_1_string_to_integer: Success\n");
}

void test_2_string_to_integer() {
    // Test case: "   -42" -> -42
    int result = myAtoi("   -42");
    assert(result == -42);
    printf("Testing: test_2_string_to_integer: Success\n");
}

void test_3_string_to_integer() {
    // Test case: "4193 with words" -> 4193
    int result = myAtoi("4193 with words");
    assert(result == 4193);
    printf("Testing: test_3_string_to_integer: Success\n");
}

void test_4_string_to_integer() {
    // Test case: "words and 987" -> 0
    int result = myAtoi("words and 987");
    assert(result == 0);
    printf("Testing: test_4_string_to_integer: Success\n");
}

void test_5_string_to_integer() {
    // Test case: "-91283472332" -> -2147483648 (overflow)
    int result = myAtoi("-91283472332");
    assert(result == -2147483648);
    printf("Testing: test_5_string_to_integer: Success\n");
}

void test_6_string_to_integer() {
    // Test case: "0-1" -> 0
    int result = myAtoi("0-1");
    assert(result == 0);
    printf("Testing: test_6_string_to_integer: Success\n");
}

void run_string_to_integer_tests() {
    printf("Running String to Integer Tests...\n");
    test_1_string_to_integer();
    test_2_string_to_integer();
    test_3_string_to_integer();
    test_4_string_to_integer();
    test_5_string_to_integer();
    test_6_string_to_integer();
    printf("All String to Integer tests completed successfully!\n\n");
} 