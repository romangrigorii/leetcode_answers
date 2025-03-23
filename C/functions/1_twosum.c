// 1: https://leetcode.com/problems/two-sum/description/
// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.

#include "headers.h"
#include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    *returnSize = 0;
    int* result = malloc(sizeof(int) * 2);
    for (int i = 0; i<numsSize; i++){
        for (int j = i+1;j<numsSize;j++){
            if (nums[i]+nums[j]==target){
                result = malloc(sizeof(int) * 2);
                if (result){
                    result[0] = i;
                    result[1] = j;
                    *returnSize = 2;
                    return result;
                }
            }
        }
    }
    return result;
}