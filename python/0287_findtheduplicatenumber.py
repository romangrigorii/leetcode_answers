import unittest
from typing import Optional, List
from general.interview.leetcode.helpers import ListNode

class RemoveElement(ListNode):
    '''
    287: https://leetcode.com/problems/find-the-duplicate-number/description/
    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
    There is only one repeated number in nums, return this repeated number.
    You must solve the problem without modifying the array nums and uses only constant extra space.
    '''
    def sol1(self, nums: List[int]) -> int:
        n = len(nums)
        left=1
        right=n-1
         
        while(left<right):
            mid=(left+right)//2;
            c=0;
            for i in range(0,n):
                if(nums[i]<=mid):
                    c+=1
            if(c>mid):
                right=mid
            else:
                left=mid+1
        return left

    def sol2(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            idx = abs(nums[i])-1
            if nums[idx] < 0: 
                return idx+1
            else: 
                nums[idx] = -nums[idx]
            

 
class test(unittest.TestCase, RemoveElement, ListNode):
    def test_(self):
        self.assertEqual(self.sol1([1,3,4,2,2]), 2)
        self.assertEqual(self.sol1([3,1,3,4,2]), 3)
        self.assertEqual(self.sol1([3,3,3,3,3]), 3)
    def test_2(self):
        self.assertEqual(self.sol2([1,3,4,2,2]), 2)
        self.assertEqual(self.sol2([3,1,3,4,2]), 3)
        self.assertEqual(self.sol2([3,3,3,3,3]), 3)
if __name__ == "__main__":
    unittest.main()