import unittest
from typing import Optional, List
from helpers import *

class _ (Helpers):
    '''
    4: https://leetcode.com/problems/median-of-two-sorted-arrays/description/
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
    The overall run time complexity should be O(log (m+n))
    '''
    def sol1(self, nums1: List[int], nums2: List[int]) -> float: # this is not a log(n+m) time
        L1, L2 = len(nums1), len(nums2)
        L = L1 + L2
        i1 = i2 = 0
        median = 0
        norm = L%2 == 0
        while (i1+i2) != (L-1)//2:
            if i2==L2 or (i1<L1 and nums1[i1] <= nums2[i2]):
                i1+=1
            else:
                i2+=1
        for q in range(norm+1):
            if i1>=L1 or (i2<L2 and nums2[i2] <= nums1[i1]):
                median+=nums2[i2]
                i2+=1
            elif i2>=L2 or (i1<L1 and nums1[i1] <= nums2[i2]):
                median+=nums1[i1]
                i1+=1
        return median/(norm+1)
    
    def sol2(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        this is a log(n+m) time algorithm
        '''
        def findkth(nums1, nums2, k):
            L1 = len(nums1)
            L2 = len(nums2)
            # these are terminating conditions
            if (L1<L2): 
                return findkth(nums2, nums1, k) # reposition so longer array is first
            if L2 == 0: 
                return nums1[k-1] # we simply take the kth element, 0 indexed
            if k == 1: 
                return min([nums1[0], nums2[0]]) # if we are at the start of the array we just find the smaller of the two, since it would come earlier in a sequence

            j = min(L2, k//2) # L2 < L1 always
            i = k - j
            if nums1[i-1]>nums2[j-1]: 
                return findkth(nums1[:i], nums2[j:], i)
            return findkth(nums1[i:], nums2, j)
        
        L1 = len(nums1)
        L2 = len(nums2)
        k = findkth(nums1, nums2, (L1+L2)//2+1)
        if (L2+L1)%2 == 0:
            k += findkth(nums1,nums2, (L1+L2)//2)
            return k/2
        return k
        
class test(unittest.TestCase, _ , Helpers):
    def test_1(self):
        self.assertEqual(self.sol1([1,3], [2]), 2)
        self.assertEqual(self.sol1([1,2], [3,4]), 2.5)
    def test_2(self):
        self.assertEqual(self.sol2([1,3], [2]), 2)
        self.assertEqual(self.sol2([1,2], [3,4]), 2.5)

if __name__ == "__main__":
    unittest.main()