import unittest
from typing import Optional, List
from helpers import *
from collections import Counter

class _ :
    '''
    This problem is an inspired one. Heres the original:

    80: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
    Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element
    appears at most twice. The relative order of the elements should be kept the same.
    Since it is impossible to change the length of the array in some languages, you must instead have the 
    result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, 
    then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
    Return k after placing the final result in the first k slots of nums.
    Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

    This problem involves sorting an UNSORTED ARRAY by twos

    '''
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for n in nums:
            if i<2 or nums[i-2]<n:
                nums[i] = n
                i+=1
        return nums

    def removeDuplicates2(self, nums: List[int]) -> int:
        if len(nums)<2: 
            if nums[0]>nums[1]: nums[0], nums[1] = nums[1], nums[0]
            return nums
        
        slow_old = 2
        slow_new = 0
        fast = 2
        while slow_old != slow_new:
            slow_new = slow_old
            fast = slow_new
            while fast<=len(nums):
                if nums[slow_new-2]<nums[fast]:
                    nums[slow_new] = nums[fast]
                    slow_new+=1
                fast+=1
        return nums


class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.removeDuplicates, self.removeDuplicates2]:
            self.assertEqual(sol([1,2,1,3,1,2])[:5], [1,1,2,2,3])

if __name__ == "__main__":
    unittest.main()
