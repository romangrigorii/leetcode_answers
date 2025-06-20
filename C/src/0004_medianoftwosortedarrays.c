// 4: https://leetcode.com/problems/median-of-two-sorted-arrays/
// Given two sorted arrays nums1 and nums2 of size m and n respectively, 
// return the median of the two sorted arrays.
// The overall run time complexity should be O(log (m+n))

#include "headers.h"
#include <stdlib.h>

// Helper function to find kth element
int findKthElement(int* nums1, int nums1Size, int* nums2, int nums2Size, int k) {
    // Ensure nums1 is the smaller array
    if (nums1Size > nums2Size) {
        return findKthElement(nums2, nums2Size, nums1, nums1Size, k);
    }
    
    // Base cases
    if (nums1Size == 0) {
        return nums2[k - 1];
    }
    if (k == 1) {
        return (nums1[0] < nums2[0]) ? nums1[0] : nums2[0];
    }
    
    // Divide and conquer
    int i = (nums1Size < k/2) ? nums1Size : k/2;
    int j = k - i;
    
    if (nums1[i-1] > nums2[j-1]) {
        return findKthElement(nums1, i, nums2 + j, nums2Size - j, k - j);
    } else {
        return findKthElement(nums1 + i, nums1Size - i, nums2, j, k - i);
    }
}

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int totalSize = nums1Size + nums2Size;
    
    if (totalSize % 2 == 1) {
        // Odd number of elements
        return (double)findKthElement(nums1, nums1Size, nums2, nums2Size, (totalSize + 1) / 2);
    } else {
        // Even number of elements
        int left = findKthElement(nums1, nums1Size, nums2, nums2Size, totalSize / 2);
        int right = findKthElement(nums1, nums1Size, nums2, nums2Size, totalSize / 2 + 1);
        return (left + right) / 2.0;
    }
} 