#include <stdio.h>
#include "src/headers.h"
#include <assert.h>

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
    printf("Testing: %s test 1: Success",  __func__);
}

int main()
{
    test_1_two_sum();
}