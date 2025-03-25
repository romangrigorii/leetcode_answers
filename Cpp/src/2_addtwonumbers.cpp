// 2: https://leetcode.com/problems/add-two-numbers/
//     You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
//     and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
//     You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#include "headers.hpp"
#include <stdlib.h>
#include <map>
#include <vector>
#include "tests/helpers.hpp"

using namespace::std;

ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    int rem = 0;
    ListNode *node = new ListNode();
    auto node_copy = node;
    while (rem!=0 || l1 || l2){
        node->next = new ListNode();
        node = node->next;
        if (l1) {
            rem += l1->val;
            l1 = l1->next;
        }
        if (l2) {
            rem += l2->val;
            l2 = l2->next;
        }
        node->val = rem%10;
        rem /= 10;
    }
    return node_copy->next;
}
