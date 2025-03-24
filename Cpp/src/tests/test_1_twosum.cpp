#include <gtest/gtest.h>
#include "../headers.hpp"
#include "helpers.hpp"
#include <vector>
#include <map>

using namespace::std;


TEST(TestSuite, TwoSum) { 
    Helpers<int> helpers;
    int target;
    vector<int> nums;
    vector<int> result_exp;
    vector<int> result_act;

    nums = {1,5,3,8,0,4,3};    

    target = 4;
    result_act = twoSum(nums, target);
    result_exp = {0, 2}; 
    helpers.COMPARE_VECS(result_act, result_exp);
    
    target = 8;
    result_act = twoSum(nums, target);
    result_exp = {1, 2}; 
    helpers.COMPARE_VECS(result_act, result_exp);
}