#include <gtest/gtest.h>
#include "src/headers.hpp"
// Demonstrate some basic assertions.
TEST(TestSuite, TwoSum) {
  
    int nums[] = {1,5,3,8,0,4,3};
    int target = 4;
    int size = sizeof(nums)/sizeof(nums[0]);
    int returnSize = -1;
    int * result = twoSum(nums, size, target, &returnSize);
    
    EXPECT_EQ(returnSize, 2);
    int result_exp[] = {0,2};
    for (int i = 0; i < 2; ++i) {
       EXPECT_EQ(result[i], result_exp[i]);
    }
}