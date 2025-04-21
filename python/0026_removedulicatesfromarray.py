import unittest
from typing import Optional, List
from helpers import *

class _ (ListNode):
    '''
    26: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
    Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
    The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
    Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
    Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
    The remaining elements of nums are not important as well as the size of nums.
    Return k.
    '''
    def sol1(self, nums: List[int]) -> int:
        if not nums: return 0     
        q = 1   
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[q] = nums[i]
                q+=1
        return nums

            
 
class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        for sol in [self.sol1]:
            self.assertEqual(sol([1,1,2])[:2], [1,2])
            self.assertEqual(sol([1,1,1,2,2,3,4,4,4,5,5,5,5,6,7,8,8,8,8])[:8], [1,2,3,4,5,6,7,8])
if __name__ == "__main__":
    unittest.main()