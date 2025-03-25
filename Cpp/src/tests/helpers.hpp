#pragma once

#include <string>
#include <vector>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

template<typename T>
class Helpers
{
public:
    void printThis(T val);
    void COMPARE_LN(ListNode * l1, ListNode *l2);
};

ListNode* vecToLN(std::vector<int> & vec);
void printLN(ListNode* node);

void COMPARE_VECS_INT(std::vector<int>& vec1, std::vector<int>& vec2);
void COMPARE_VECS_STR(std::vector<std::string>& vec1, std::vector<std::string>& vec2);