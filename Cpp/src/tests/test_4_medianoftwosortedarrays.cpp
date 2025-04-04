#include <gtest/gtest.h>
#include "../headers.hpp"
#include "helpers.hpp"
#include <vector>
#include <map>
#include <string>

using namespace::std;

void test(vector<int> vec1, vector<int> vec2, double exp){
    double act = findMedianSortedArrays(vec1, vec2);
    EXPECT_DOUBLE_EQ(act, exp);
}

TEST(TestSuite, MedianOfSortedArrays) {
    test({1,3}, {2}, 2.0);
    test({1,2}, {3,4}, 2.5);
}