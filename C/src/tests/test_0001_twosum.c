#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "../headers.h"

void test_1_two_sum(){
    // test 1
    int nums[] = {1,5,3,8,0,4,3};
    int target = 4;
    int size = sizeof(nums)/sizeof(nums[0]);
    int returnSize = -1;
    int * result = twoSum(nums, size, target, &returnSize);
    
    assert(returnSize==2);
    if (returnSize==2){
        assert(result[0]==0 && result[1]==2 || result[0]==2 && result[1]==0);
    }
    printf("Testing: %s test 1: Success\n",  __func__);
    
    // Free allocated memory
    if (result) {
        free(result);
    }
}

// Function to run all two sum tests
void run_two_sum_tests() {
    printf("Running Two Sum Tests...\n");
    test_1_two_sum();
    printf("All Two Sum tests completed successfully!\n\n");
} 