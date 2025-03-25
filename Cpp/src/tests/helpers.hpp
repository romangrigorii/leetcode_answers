#pragma once

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
    void COMPARE_VECS(std::vector<T>& vec1, std::vector<T>& vec2);
    void COMPARE_LN(ListNode * l1, ListNode *l2);
};

ListNode* vecToLN(std::vector<int> & vec);
void printLN(ListNode* node);