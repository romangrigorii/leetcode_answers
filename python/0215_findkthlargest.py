import unittest
from typing import Optional, List
from helpers import ListNode


# class FindKthSmallestNumberTwoArrays:
#     def sol1(self, nums1, nums2, k):
#         '''
#         Given lists nums1 and nums2 find the kth smallest number among them        
#         '''
#         L1 = len(nums1)
#         L2 = len(nums2)
#         # these are terminating conditions
#         if (L1<L2): return self.sol1(nums2, nums1, k)
#         if L2 == 0: return nums1[k-1]
#         if k == 1: return min([nums1[0], nums2[0]])

#         j = min(L2, k//2) # L2 < L1 always
#         i = k - j
#         if nums1[i-1]>nums2[j-1]: 
#             return self.sol1(nums1[:i], nums2[j:], k-j)
#         return self.sol1(nums1[i:], nums2, k-i)

# class test(unittest.TestCase, FindKthLargestElement, ListNode):
#     def test_1(self):
#         self.assertEqual(self.sol1([1,2,4,8], [3,5,6,7], 2), 2) 
#         self.assertEqual(self.sol1([1,2,4,8], [3,5,6,7], 4), 4) 

class FindKthSmallestElement:
    def sol1(self, nums, k):
        '''
        This strategy uses QuickSelect algorithm
        '''
        if not nums: return
        pivot = nums[0]
        left = [x for x in nums if x < pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]
        L = len(left)
        M = len(mid)

        if k <= L:
            return self.sol1(left, k)
        elif k > L+M:
            return self.sol1(right, k - M - L)
        return mid[0]

class test(unittest.TestCase, FindKthSmallestElement, ListNode):
    def test_1(self):
        self.assertEqual(self.sol1([3,2,1,5,6,4], 2), 2) 
        self.assertEqual(self.sol1([3,2,3,1,2,4,5,5,6], 4), 3) 

if __name__ == "__main__":
    unittest.main()