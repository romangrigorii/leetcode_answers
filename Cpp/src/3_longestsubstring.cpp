// 3: https://leetcode.com/problems/longest-substring-without-repeating-characters/
// Given a string s, find the length of the longest substring without repeating characters.

#include "headers.hpp"
#include <stdlib.h>
#include <map>
#include <vector>
#include "tests/helpers.hpp"

using namespace::std;

int lengthOfLongestSubstring(string s){
    std::map<char,int> appearance;
    int st = -1; // starting index
    int longest = 1;
    for (int i = 0; i < s.size(); i++){
        if (appearance.end() != appearance.find(s[i])){
            st = max(st, appearance[s[i]]);
        }
        longest = max(longest, i-st);
        appearance[s[i]] = i;
    }
    return longest;
}