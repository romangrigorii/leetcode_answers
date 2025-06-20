// Linked list structure
struct ListNode {
    int val;
    struct ListNode *next;
};

// Algorithm function declarations
int* twoSum(int* nums, int numsSize, int target, int* returnSize);
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2);
int lengthOfLongestSubstring(char* s);
double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size);
char* longestPalindrome(char* s);
char* convert(char* s, int numRows);
int reverse(int x);
int myAtoi(char* s);
int isPalindrome(int x);
int isMatch(char* s, char* p);

// Helper function declarations
struct ListNode* createListNode(int val);
struct ListNode* arrayToList(int* arr, int size);
int* listToArray(struct ListNode* head, int* size);
void freeList(struct ListNode* head);
int compareArrays(int* arr1, int size1, int* arr2, int size2);

// Test function declarations
void run_two_sum_tests();
void run_add_two_numbers_tests();
void run_longest_substring_tests();
void run_median_sorted_arrays_tests();
void run_longest_palindrome_tests();
void run_zigzag_conversion_tests();
void run_reverse_integer_tests();
void run_string_to_integer_tests();
void run_palindrome_number_tests();
void run_regular_expression_matching_tests();