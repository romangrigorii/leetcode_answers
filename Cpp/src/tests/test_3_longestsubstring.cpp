#include <gtest/gtest.h>
#include "../headers.hpp"
#include "helpers.hpp"
#include <vector>
#include <map>
#include <string>

using namespace::std;


TEST(TestSuite, LengthOfLongestSubstring) { 
    int res;
    int exp;
    res = lengthOfLongestSubstring("abcabcbb");
    exp = 3;
    EXPECT_EQ(res, exp);
    res = lengthOfLongestSubstring("bbbbb");
    exp = 1;
    EXPECT_EQ(res, exp);
    res = lengthOfLongestSubstring("pwwkew");
    exp = 3;
    EXPECT_EQ(res, exp);
}