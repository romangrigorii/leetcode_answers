import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    167: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

    Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

    Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

    The tests are generated such that there is exactly one solution. You may not use the same element twice.

    Your solution must use only constant extra space.

    '''
    def sol1(self, numbers: List[int], target: int) -> List[int]:
        i= 0
        j= len(numbers)-1
        while i!=j :
            if numbers[i]+numbers[j]>target:
                j=j-1
            elif numbers[i]+numbers[j]<target:
                i=i+1
            else:
                return [i+1,j+1] 
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol([2,7,11,15], 9), [1,2])
            self.assertEqual(sol([2,3,4], 6), [1,3])
            self.assertEqual(sol([-1, 0], -1), [1,2])

if __name__ == "__main__":
    unittest.main()
