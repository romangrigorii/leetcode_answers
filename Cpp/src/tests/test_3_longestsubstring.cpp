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
<<<<<<< HEAD
    test("abcabcbb", 3);
    test("bbbbb", 1);
    test("pwwkew", 3);
=======
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
>>>>>>> 568d50a (Solving problem 4 in Cpp)
}