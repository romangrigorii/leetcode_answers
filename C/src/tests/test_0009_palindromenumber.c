#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "../headers.h"

void test_1_palindrome_number() {
    // Test case: 121 -> true
    int result = isPalindrome(121);
    assert(result == 1);
    printf("Testing: test_1_palindrome_number: Success\n");
}

void test_2_palindrome_number() {
    // Test case: -121 -> false
    int result = isPalindrome(-121);
    assert(result == 0);
    printf("Testing: test_2_palindrome_number: Success\n");
}

void test_3_palindrome_number() {
    // Test case: 10 -> false
    int result = isPalindrome(10);
    assert(result == 0);
    printf("Testing: test_3_palindrome_number: Success\n");
}

void test_4_palindrome_number() {
    // Test case: 0 -> true
    int result = isPalindrome(0);
    assert(result == 1);
    printf("Testing: test_4_palindrome_number: Success\n");
}

void test_5_palindrome_number() {
    // Test case: 12321 -> true
    int result = isPalindrome(12321);
    assert(result == 1);
    printf("Testing: test_5_palindrome_number: Success\n");
}

void test_6_palindrome_number() {
    // Test case: 12345 -> false
    int result = isPalindrome(12345);
    assert(result == 0);
    printf("Testing: test_6_palindrome_number: Success\n");
}

void run_palindrome_number_tests() {
    printf("Running Palindrome Number Tests...\n");
    test_1_palindrome_number();
    test_2_palindrome_number();
    test_3_palindrome_number();
    test_4_palindrome_number();
    test_5_palindrome_number();
    test_6_palindrome_number();
    printf("All Palindrome Number tests completed successfully!\n\n");
} 