#include <gtest/gtest.h>
#include "../headers.hpp"
#include "helpers.hpp"
#include <vector>
#include <map>
#include <string>
#include <algorithm>

TEST(TestSuite, GenerateParantheses) {
    Helpers<string> helpers;
    vector<string> exp;
    vector<string> res;
    exp = {"()"};
    res = generateParentheses(1);
    COMPARE_VECS_STR(res, exp);

    exp = {"()()", "(())"};
    res = generateParentheses(2);
    COMPARE_VECS_STR(res, exp);

    exp = {"()()()", "(())()", "()(())", "((()))","(()())"};
    res = generateParentheses(3);
    COMPARE_VECS_STR(res, exp);
}