#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "../headers.h"

void test_1_add_two_numbers() {
    // Test case: [2,4,3] + [5,6,4] = [7,0,8]
    int arr1[] = {2, 4, 3};
    int arr2[] = {5, 6, 4};
    int expected[] = {7, 0, 8};
    
    struct ListNode* l1 = arrayToList(arr1, 3);
    struct ListNode* l2 = arrayToList(arr2, 3);
    
    struct ListNode* result = addTwoNumbers(l1, l2);
    int resultSize;
    int* resultArr = listToArray(result, &resultSize);
    
    assert(compareArrays(resultArr, resultSize, expected, 3));
    printf("Testing: test_1_add_two_numbers: Success\n");
    
    // Cleanup
    freeList(l1);
    freeList(l2);
    freeList(result);
    free(resultArr);
}

void test_2_add_two_numbers() {
    // Test case: [0] + [0] = [0]
    int arr1[] = {0};
    int arr2[] = {0};
    int expected[] = {0};
    
    struct ListNode* l1 = arrayToList(arr1, 1);
    struct ListNode* l2 = arrayToList(arr2, 1);
    
    struct ListNode* result = addTwoNumbers(l1, l2);
    int resultSize;
    int* resultArr = listToArray(result, &resultSize);
    
    assert(compareArrays(resultArr, resultSize, expected, 1));
    printf("Testing: test_2_add_two_numbers: Success\n");
    
    // Cleanup
    freeList(l1);
    freeList(l2);
    freeList(result);
    free(resultArr);
}

void test_3_add_two_numbers() {
    // Test case: [9,9,9,9,9,9,9] + [9,9,9,9] = [8,9,9,9,0,0,0,1]
    int arr1[] = {9, 9, 9, 9, 9, 9, 9};
    int arr2[] = {9, 9, 9, 9};
    int expected[] = {8, 9, 9, 9, 0, 0, 0, 1};
    
    struct ListNode* l1 = arrayToList(arr1, 7);
    struct ListNode* l2 = arrayToList(arr2, 4);
    
    struct ListNode* result = addTwoNumbers(l1, l2);
    int resultSize;
    int* resultArr = listToArray(result, &resultSize);
    
    assert(compareArrays(resultArr, resultSize, expected, 8));
    printf("Testing: test_3_add_two_numbers: Success\n");
    
    // Cleanup
    freeList(l1);
    freeList(l2);
    freeList(result);
    free(resultArr);
}

void run_add_two_numbers_tests() {
    printf("Running Add Two Numbers Tests...\n");
    test_1_add_two_numbers();
    test_2_add_two_numbers();
    test_3_add_two_numbers();
    printf("All Add Two Numbers tests completed successfully!\n\n");
} 