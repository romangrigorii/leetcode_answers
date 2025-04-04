import unittest
from typing import Optional, List
from helpers import *

class _ (Helpers):
    '''
    31: https://leetcode.com/problems/next-permutation/description/
    A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
    For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]. 
    The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 
    More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, 
    then the next permutation of that array is the permutation that follows it in the sorted container. 
    If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).
    For example, the next permutation of arr = [1,2,3] is [1,3,2].
    Similarly, the next permutation of arr = [2,3,1] is [3,1,2]. 
    While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
    Given an array of integers nums, find the next permutation of nums.
    The replacement must be in place and use only constant extra memory..
    '''
    def sol1(self, nums: List[int]):
        l = 0
        r = len(nums)-1
        while r>l:
            if nums[r]>nums[r-1]:
                i = r+1
                imin = r
                while i<len(nums):
                    if nums[i]>nums[r-1] and nums[i]<nums[imin]:
                        imin = i
                    i+=1
                nums[imin], nums[r-1] = nums[r-1], nums[imin]
                break
            else:
                r -= 1

        q = nums[r:]
        q.sort()
        nums[r:] = q      
        return nums
    
    def sol2(self, nums: List[int]):
        i = j = len(nums)-1
        # First we'll find the first non-increasing element starting from the end
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        # After completion of the first loop, there will be two cases
        # 1. Our i becomes zero (This will happen if the given array is sorted decreasingly). In this case, we'll simply reverse the sequence and will return 
        if i == 0:
            nums.reverse()
            return nums
        # 2. If it's not zero then we'll find the first number greater than nums[i-1] starting from end
        while nums[j] <= nums[i-1]:
            j -= 1
        # Now out pointer is pointing at two different positions
        # i. first non-assending number from end
        # j. first number greater than nums[i-1]
        
        # We'll swap these two numbers
        nums[i-1], nums[j] = nums[j], nums[i-1]
        
        # We'll reverse a sequence strating from i to end
        nums[i:]= nums[len(nums)-1:i-1:-1]
        # We don't need to return anything as we've modified nums in-place
        return nums
 
class test(unittest.TestCase, _, Helpers):
    def test_1(self):
        self.assertEqual(self.sol1([1,2,3]), [1,3,2])
        self.assertEqual(self.sol1([3,2,1]), [1,2,3])
        self.assertEqual(self.sol1([1,1,5]), [1,5,1])
    def test_2(self):
        self.assertEqual(self.sol2([1,2,3]), [1,3,2])
        self.assertEqual(self.sol2([3,2,1]), [1,2,3])
        self.assertEqual(self.sol2([1,1,5]), [1,5,1])
        self.assertEqual(self.sol2([1,4,3,2]), [2,1,3,4])
        self.assertEqual(self.sol2([1,4,5,3,2]), [1,5,2,3,4])
if __name__ == "__main__":
    unittest.main()