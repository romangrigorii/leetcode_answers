#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "../headers.h"

void test_1_reverse_integer() {
    // Test case: 123 -> 321
    int result = reverse(123);
    assert(result == 321);
    printf("Testing: test_1_reverse_integer: Success\n");
}

void test_2_reverse_integer() {
    // Test case: -123 -> -321
    int result = reverse(-123);
    assert(result == -321);
    printf("Testing: test_2_reverse_integer: Success\n");
}

void test_3_reverse_integer() {
    // Test case: 120 -> 21
    int result = reverse(120);
    assert(result == 21);
    printf("Testing: test_3_reverse_integer: Success\n");
}

void test_4_reverse_integer() {
    // Test case: 0 -> 0
    int result = reverse(0);
    assert(result == 0);
    printf("Testing: test_4_reverse_integer: Success\n");
}

void test_5_reverse_integer() {
    // Test case: overflow case -> 0
    int result = reverse(1534236469);
    assert(result == 0);
    printf("Testing: test_5_reverse_integer: Success\n");
}

void test_6_reverse_integer() {
    // Test case: negative overflow case -> 0
    int result = reverse(-2147483648);
    assert(result == 0);
    printf("Testing: test_6_reverse_integer: Success\n");
}

void run_reverse_integer_tests() {
    printf("Running Reverse Integer Tests...\n");
    test_1_reverse_integer();
    test_2_reverse_integer();
    test_3_reverse_integer();
    test_4_reverse_integer();
    test_5_reverse_integer();
    test_6_reverse_integer();
    printf("All Reverse Integer tests completed successfully!\n\n");
} 