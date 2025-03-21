import unittest
from typing import Optional, List
from helpers import *
from collections import Counter

class _ :
    '''
    80: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
    Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element
    appears at most twice. The relative order of the elements should be kept the same.
    Since it is impossible to change the length of the array in some languages, you must instead have the 
    result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, 
    then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
    Return k after placing the final result in the first k slots of nums.
    Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
    '''
    def sol1(self, nums: List[int]) -> int:
        i = 0
        for n in nums:
            if i<2 or nums[i-2]<n:
                nums[i] = n
                i+=1
        return nums

    def sol2(self, nums: List[int]) -> int:
        c = Counter(nums)
        i, n = 0, 0
        while i < len(nums):
            if c[nums[i]]>2:
                nums[n] = nums[i]
                nums[n+1] = nums[i+1]
                n+=2
                i+=c[nums[i]]
            else:
                nums[n] = nums[i]
                n+=1
                i+=1
        return nums


class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.sol1, self.sol2]:
            self.assertEqual(sol([1,1,1,2,2,3])[:5], [1,1,2,2,3])

if __name__ == "__main__":
    unittest.main()
