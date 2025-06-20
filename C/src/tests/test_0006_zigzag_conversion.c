#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include "../headers.h"

void test_1_zigzag_conversion() {
    // Test case: "PAYPALISHIRING", 3 -> "PAHNAPLSIIGYIR"
    char* s = "PAYPALISHIRING";
    char* result = convert(s, 3);
    assert(strcmp(result, "PAHNAPLSIIGYIR") == 0);
    printf("Testing: test_1_zigzag_conversion: Success\n");
    free(result);
}

void test_2_zigzag_conversion() {
    // Test case: "PAYPALISHIRING", 4 -> "PINALSIGYAHRPI"
    char* s = "PAYPALISHIRING";
    char* result = convert(s, 4);
    assert(strcmp(result, "PINALSIGYAHRPI") == 0);
    printf("Testing: test_2_zigzag_conversion: Success\n");
    free(result);
}

void test_3_zigzag_conversion() {
    // Test case: "A", 1 -> "A"
    char* s = "A";
    char* result = convert(s, 1);
    assert(strcmp(result, "A") == 0);
    printf("Testing: test_3_zigzag_conversion: Success\n");
    free(result);
}

void test_4_zigzag_conversion() {
    // Test case: "AB", 1 -> "AB"
    char* s = "AB";
    char* result = convert(s, 1);
    assert(strcmp(result, "AB") == 0);
    printf("Testing: test_4_zigzag_conversion: Success\n");
    free(result);
}

void test_5_zigzag_conversion() {
    // Test case: "ABC", 2 -> "ACB"
    char* s = "ABC";
    char* result = convert(s, 2);
    assert(strcmp(result, "ACB") == 0);
    printf("Testing: test_5_zigzag_conversion: Success\n");
    free(result);
}

void run_zigzag_conversion_tests() {
    printf("Running Zigzag Conversion Tests...\n");
    test_1_zigzag_conversion();
    test_2_zigzag_conversion();
    test_3_zigzag_conversion();
    test_4_zigzag_conversion();
    test_5_zigzag_conversion();
    printf("All Zigzag Conversion tests completed successfully!\n\n");
} 