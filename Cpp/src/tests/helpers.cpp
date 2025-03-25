#include <gtest/gtest.h>
#include <vector>
#include <map>
#include "helpers.hpp"
#include <algorithm>
#include <iostream>

bool comp(int a, int b) {
    return a > b;
}

template <typename T>
void Helpers<T>::printThis(T val){
    std::cout << val << std::endl;
}

template <typename T>
void Helpers<T>::COMPARE_VECS(std::vector<T>& vec1, std::vector<T>& vec2){
    EXPECT_EQ(vec1.size(), vec2.size());
    sort(vec1.begin(), vec1.end(), comp);
    sort(vec2.begin(), vec2.end(), comp);
    for (int i = 0; i<vec1.size(); i++){
        EXPECT_EQ(vec1[i], vec2[i]);
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

ListNode* vecToLN(std::vector<int> & vec){
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