import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    66: https://leetcode.com/problems/plus-one/description/
    You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
    The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain 
    any leading 0's. 
    Increment the large integer by one and return the resulting array of digits.

    '''
    def plusOne(self, digits: List[int]) -> List[int]:
        for q in range(len(digits)-1,-1,-1):
            if digits[q]<9: 
                digits[q]+=1
                return digits
            else:
                digits[q] = 0
        return [1] + digits

    
class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.plusOne]:
            self.assertEqual(sol([1,2,3]), [1,2,4])
            self.assertEqual(sol([9,0,9,9]), [9,1,0,0])

if __name__ == "__main__":
    unittest.main()
