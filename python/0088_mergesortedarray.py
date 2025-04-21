import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    88: https://leetcode.com/problems/merge-sorted-array/
    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
    representing the number of elements in nums1 and nums2 respectively.
    Merge nums1 and nums2 into a single array sorted in non-decreasing order.
    The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
    To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
    and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
    '''
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, writing = m-1, n-1, m+n-1
        while j>=0:
            if i>=0 and nums1[i]>nums2[j]:
                nums1[writing] = nums1[i]
                i-=1
            else:
                nums1[writing] = nums2[j]
                j-=1
            writing -=1
        return nums1


class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.merge]:
            self.assertEqual(sol([1,2,3,0,0,0], 3,  [2,5,6], 3), [1,2,2,3,5,6])
            self.assertEqual(sol([4,5,6,0,0,0], 3,  [1,2,3], 3), [1,2,3,4,5,6])
            self.assertEqual(sol([4,0,0,0,0,0], 1,  [1,2,3,5,6], 5), [1,2,3,4,5,6])
if __name__ == "__main__":
    unittest.main()
