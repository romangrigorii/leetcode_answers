#include <gtest/gtest.h>
#include "../headers.hpp"
#include "helpers.hpp"
#include <vector>
#include <map>
#include <string>

using namespace::std;


TEST(TestSuite, FindMedianSortedArrays) {
    std::vector<int> vec1;
    std::vector<int> vec2;
    int res;
    int exp;

    vec1 = {1,3};
    vec2 = {2};
    res = findMedianSortedArrays(vec1, vec2);
    exp = 2.0000;
    EXPECT_DOUBLE_EQ(res, exp);

    vec1 = {1,2};
    vec2 = {3,4};
    res = findMedianSortedArrays(vec1, vec2);
    exp = 2.5;
    EXPECT_DOUBLE_EQ(res, exp);
}