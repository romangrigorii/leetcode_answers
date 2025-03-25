#include <gtest/gtest.h>
#include "../headers.hpp"
#include "helpers.hpp"
#include <vector>
#include <map>

using namespace::std;


TEST(TestSuite, LengthOfLongestSubstring) { 
    auto res = lengthOfLongestSubstring("abcabcbb");
    auto exp = 4;
    COMPARE_EQ(res, exp);
}