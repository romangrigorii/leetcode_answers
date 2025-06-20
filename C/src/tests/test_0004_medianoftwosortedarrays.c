#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <math.h>
#include "../headers.h"

void test_1_median_sorted_arrays() {
    // Test case: [1,3], [2] -> 2.0
    int nums1[] = {1, 3};
    int nums2[] = {2};
    double result = findMedianSortedArrays(nums1, 2, nums2, 1);
    assert(fabs(result - 2.0) < 0.001);
    printf("Testing: test_1_median_sorted_arrays: Success\n");
}

void test_2_median_sorted_arrays() {
    // Test case: [1,2], [3,4] -> 2.5
    int nums1[] = {1, 2};
    int nums2[] = {3, 4};
    double result = findMedianSortedArrays(nums1, 2, nums2, 2);
    assert(fabs(result - 2.5) < 0.001);
    printf("Testing: test_2_median_sorted_arrays: Success\n");
}

void test_3_median_sorted_arrays() {
    // Test case: [0,0], [0,0] -> 0.0
    int nums1[] = {0, 0};
    int nums2[] = {0, 0};
    double result = findMedianSortedArrays(nums1, 2, nums2, 2);
    assert(fabs(result - 0.0) < 0.001);
    printf("Testing: test_3_median_sorted_arrays: Success\n");
}

void test_4_median_sorted_arrays() {
    // Test case: [], [1] -> 1.0
    int nums1[] = {};
    int nums2[] = {1};
    double result = findMedianSortedArrays(nums1, 0, nums2, 1);
    assert(fabs(result - 1.0) < 0.001);
    printf("Testing: test_4_median_sorted_arrays: Success\n");
}

void test_5_median_sorted_arrays() {
    // Test case: [2], [] -> 2.0
    int nums1[] = {2};
    int nums2[] = {};
    double result = findMedianSortedArrays(nums1, 1, nums2, 0);
    assert(fabs(result - 2.0) < 0.001);
    printf("Testing: test_5_median_sorted_arrays: Success\n");
}

void run_median_sorted_arrays_tests() {
    printf("Running Median of Two Sorted Arrays Tests...\n");
    test_1_median_sorted_arrays();
    test_2_median_sorted_arrays();
    test_3_median_sorted_arrays();
    test_4_median_sorted_arrays();
    test_5_median_sorted_arrays();
    printf("All Median of Two Sorted Arrays tests completed successfully!\n\n");
} 