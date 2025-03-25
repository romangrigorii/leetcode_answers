// 5: https://leetcode.com/problems/longest-palindromic-substring/
// Given a string s, return the longest palindromic substring in s.

#include "headers.hpp"
#include <stdlib.h>
#include <map>
#include <vector>
#include "tests/helpers.hpp"
#include <string>
#include <iostream>

using namespace::std;

string longestPalindrome(string s) {
    struct Helper{
        int length(string& s, int st, int en){
            int len = 1;
            if (st==en){
                len = 1;
            }
            if (st>=0 & st<s.size() & s[st]==s[en]){
                st--;
                en++;
            }
            return en-st;
        }
    };
    int longest = 1;
    for (int i = 0; i<s.size(); i++){
        i--;
    }
    return "s";
    
}