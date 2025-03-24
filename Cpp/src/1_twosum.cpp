// 1: https://leetcode.com/problems/two-sum/description/
// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.

#include "headers.hpp"
#include <stdlib.h>
#include <map>
#include <vector>

using namespace::std;

vector<int> twoSum(vector<int>& nums, int target) {
    map<int, int> val_map;
    vector<int> ret_vals = {-1,-1}; 
    for (int i = 0; i<nums.size(); i++){
        if (val_map.find(nums[i]) == val_map.end()){
            val_map[target-nums[i]] = i;
        } else {
            ret_vals = {val_map[nums[i]], i};
            return ret_vals;
        }
    }
    return ret_vals;
}