#include <gtest/gtest.h>
#include "../headers.hpp"
#include "helpers.hpp"
#include <vector>
#include <map>
#include <string>

using namespace::std;

void test(string str, int exp){
    int res = lengthOfLongestSubstring(str);
    EXPECT_EQ(res, exp);
}

TEST(TestSuite, LengthOfLongestSubstring) { 
    test("abcabcbb", 3);
    test("bbbbb", 1);
    test("pwwkew", 3);
}