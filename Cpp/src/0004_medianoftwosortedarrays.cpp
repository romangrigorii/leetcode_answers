// 4: https://leetcode.com/problems/median-of-two-sorted-arrays/
// Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
// The overall run time complexity should be O(log (m+n)).


#include "headers.hpp"
#include <stdlib.h>
#include <map>
#include <vector>
#include "tests/helpers.hpp"
#include <string>
#include <iostream>

using namespace::std;

// We have to find out when we are halfway through the list of nums
// and use that as the median

double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    auto L1 = nums1.size();
    auto L2 = nums2.size();
    int medIdx = (L1+L2)/2;
    bool even = ((L1+L2)%2) == 0;
    medIdx -= even;
    int iter1 = 0;
    int iter2 = 0;
    double res1 = 0;
    double res2 = 0;

    while ((iter1 + iter2) <= medIdx+even){
        res1 = res2;
        if (iter1==L1){
            res2 = nums2[iter2];
            iter2+=1;
        } else if (iter2==L2){
            res2 = nums1[iter1];
            iter1+=1;
        } else if (nums1[iter1]<nums2[iter2]){
            res2 = nums1[iter1];
            iter1+=1;
        } else {
            res2 = nums2[iter2];
            iter2+=1;
        }
    }
    if (even){
        return (res2+res1)/2;
    } else {
        return res2;
    }
}