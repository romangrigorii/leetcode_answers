import unittest
from typing import Optional, List
from helpers import *

class _ (ListNode):
    '''
    27: https://leetcode.com/problems/remove-element/
    Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
    The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
    Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things: 
    Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
    The remaining elements of nums are not important as well as the size of nums. Return k.
    '''
    def sol1(self, nums: List[int], val: int) -> int:
        q = -1
        for i in range(len(nums)):
            if val != nums[i]:
                q+=1
                if q<i: 
                    nums[q] = nums[i]
        return q+1  

 
class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        self.assertEqual(self.sol1([3,2,2,3], 3), 2)

if __name__ == "__main__":
    unittest.main()