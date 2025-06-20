// 2: https://leetcode.com/problems/add-two-numbers/
// You are given two non-empty linked lists representing two non-negative integers. 
// The digits are stored in reverse order, and each of their nodes contains a single digit. 
// Add the two numbers and return the sum as a linked list.
// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#include "headers.h"
#include <stdlib.h>

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* dummy = createListNode(0);
    struct ListNode* current = dummy;
    int carry = 0;
    
    while (l1 || l2 || carry) {
        int sum = carry;
        
        if (l1) {
            sum += l1->val;
            l1 = l1->next;
        }
        if (l2) {
            sum += l2->val;
            l2 = l2->next;
        }
        
        carry = sum / 10;
        current->next = createListNode(sum % 10);
        current = current->next;
    }
    
    struct ListNode* result = dummy->next;
    free(dummy);
    return result;
} 