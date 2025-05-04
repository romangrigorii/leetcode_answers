// 5: https://leetcode.com/problems/generate-parentheses/description/
// Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

#include "headers.hpp"
#include <stdlib.h>
#include <map>
#include <vector>
#include "tests/helpers.hpp"
#include <string>
#include <iostream>

using namespace::std;

vector<string> generateParentheses(int n) {
    vector<pair<string,pair<int, int>>> stack = {make_pair("", make_pair(0,0))};
    vector<string> out;
    if (n == 0) return out;
    while (stack.size()>0){
        auto elem = stack.back();
        stack.pop_back();
        if (elem.second.first==n && elem.second.second==n){
            out.push_back(string(elem.first));
        } else {
            if (elem.second.first<elem.second.second || elem.second.first>n || elem.second.second>n) continue;
            stack.push_back(make_pair(elem.first+")", make_pair(elem.second.first, elem.second.second+1)));
            stack.push_back(make_pair(elem.first+"(", make_pair(elem.second.first+1, elem.second.second)));
        }
    }
    return out;
}