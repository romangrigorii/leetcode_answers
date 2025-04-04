#include <gtest/gtest.h>
#include "../headers.hpp"
#include "helpers.hpp"
#include <vector>
#include <map>
#include <string>

using namespace::std;

void test(string palindrome, string exp){
    string act = longestPalindrome(palindrome);
    EXPECT_TRUE(exp==act);
    if (exp!=act){
        cout << "expected: " << exp << " " << "actual: " << act << endl;
    }
}

TEST(TestSuite, LongestPalindrome) {
    test("abbagi", "abba");
    test("", "");
    test("aaaaa", "aaaaa");
    test("aaaaaa", "aaaaaa");
}


