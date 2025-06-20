#include "headers.h"
#include <stdlib.h>
#include <string.h>

// Create a new ListNode with given value
struct ListNode* createListNode(int val) {
    struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
    if (node) {
        node->val = val;
        node->next = NULL;
    }
    return node;
}

// Convert array to linked list
struct ListNode* arrayToList(int* arr, int size) {
    if (size == 0) return NULL;
    
    struct ListNode* head = createListNode(arr[0]);
    struct ListNode* current = head;
    
    for (int i = 1; i < size; i++) {
        current->next = createListNode(arr[i]);
        current = current->next;
    }
    
    return head;
}

// Convert linked list to array
int* listToArray(struct ListNode* head, int* size) {
    if (!head) {
        *size = 0;
        return NULL;
    }
    
    // Count nodes
    int count = 0;
    struct ListNode* current = head;
    while (current) {
        count++;
        current = current->next;
    }
    
    *size = count;
    int* arr = (int*)malloc(count * sizeof(int));
    
    current = head;
    for (int i = 0; i < count; i++) {
        arr[i] = current->val;
        current = current->next;
    }
    
    return arr;
}

// Free linked list memory
void freeList(struct ListNode* head) {
    struct ListNode* current = head;
    while (current) {
        struct ListNode* temp = current;
        current = current->next;
        free(temp);
    }
}

// Compare two arrays
int compareArrays(int* arr1, int size1, int* arr2, int size2) {
    if (size1 != size2) return 0;
    for (int i = 0; i < size1; i++) {
        if (arr1[i] != arr2[i]) return 0;
    }
    return 1;
} 