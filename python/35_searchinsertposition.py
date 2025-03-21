import unittest
from typing import Optional, List

class Search_in_Rotated_Sorted_Array():
    '''
    35: https://leetcode.com/problems/search-insert-position/description/
    Given a sorted array of distinct integers and a target value, return the index if the target is found. 
    If not, return the index where it would be if it were inserted in order.
    You must write an algorithm with O(log n) runtime complexity.
    '''
    def sol1(self, nums: List[int], target: int) -> int:
        l = 0        
        L = len(nums)
        r = L - 1
        while l<=r:
            m = (l+r)//2
            if nums[m]==target:
                while (m+1)<L and nums[m+1]==target: 
                    m+=1
                return m
            else:
                if nums[m]<target: 
                    l = m+1
                else: 
                    r = m-1
        return l
    
class test(unittest.TestCase, Search_in_Rotated_Sorted_Array):
    def test_(self):
        self.assertEqual(self.sol1(nums = [1,3,5,6], target = 5), 2)
        self.assertEqual(self.sol1(nums = [1,3,5,6], target = 2), 1)
        self.assertEqual(self.sol1(nums = [1,3,5,6], target = 7), 4)
        self.assertEqual(self.sol1(nums = [1,3,5,6], target = 0), 0)

if __name__ == "__main__":
    unittest.main()