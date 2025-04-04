// 5: https://leetcode.com/problems/longest-palindromic-substring/
// Given a string s, return the longest palindromic substring in s.

#include "headers.hpp"
#include <stdlib.h>
#include <map>
#include <vector>
#include "tests/helpers.hpp"
#include <string>
#include <iostream>
#include <algorithm>

using namespace::std;

string longestPalindrome(string& s) {
    auto length = [](string& s, int st, int en){
        if (s[st]!=s[en]) return string("");
        while ((st-1)>=0 && (en+1)<s.size() && s[st-1]==s[en+1]){
            st--;
            en++;
        }
        return string(s.substr(st,en-st+1));
    };
    string longest = "";
    string a = "";
    string b = "";
    for (int i = 0; i<s.size(); i++){
        a = length(s,i,i);
        b = length(s,i,i+1);
        if (a.size()>longest.size()){
            longest = a;
        }
        if (b.size()>longest.size()){
            longest = b;
        }
    }
    return longest;    
}