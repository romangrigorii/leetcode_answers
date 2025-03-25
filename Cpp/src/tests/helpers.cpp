#include <gtest/gtest.h>
#include <vector>
#include <map>
#include "helpers.hpp"
#include <algorithm>
#include <iostream>
#include <string>

using namespace::std;

template <typename T>
bool comp(T a, T b) {
    return a > b;
}

template <typename T>
void Helpers<T>::printThis(T val){
    std::cout << val << std::endl;
}

void COMPARE_VECS_INT(vector<int>& vec1, vector<int>& vec2){
    EXPECT_EQ(vec1.size(), vec2.size());
    sort(vec1.begin(), vec1.end(), comp<int>);
    sort(vec2.begin(), vec2.end(), comp<int>);
    for (int i = 0; i<vec1.size(); i++){
        EXPECT_TRUE(vec1[i]==vec2[i]);
    }
}

void COMPARE_VECS_STR(vector<string>& vec1, vector<string>& vec2){
    EXPECT_EQ(vec1.size(), vec2.size());
    sort(vec1.begin(), vec1.end(), comp<string>);
    sort(vec2.begin(), vec2.end(), comp<string>);
    for (int i = 0; i<vec1.size(); i++){
        EXPECT_TRUE(vec1[i]==vec2[i]);
    }
}


template <typename T>
void Helpers<T>::COMPARE_LN(ListNode *l1, ListNode *l2){
    while (l1 || l2){
        EXPECT_NE(l1, nullptr);
        EXPECT_NE(l2, nullptr);
        EXPECT_EQ(l1->val, l2->val);
        l1 = l1->next;
        l2 = l2->next;
    }
}

template class Helpers<int>;

ListNode* vecToLN(vector<int>& vec){
    ListNode *node = new ListNode();
    auto node_copy = node;
    for (int i = 0; i < vec.size(); i++){
        node->next = new ListNode();
        node = node->next;
        node->val = vec[i];
    }
    return node_copy->next;
}

void printLN(ListNode* node){
    std::cout << "Printing Out List Node: " << std::endl;
    while (node){
        std::cout << node->val;
        if (node->next) std::cout << " - ";
        node = node->next;
    }
    std::cout << std::endl;
}