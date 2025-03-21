import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    238: https://leetcode.com/problems/product-of-array-except-self/description/
    The problem is to find product of the array entries, where at every index we find the product of 
    all other entries (not including the one at current index)
    '''
    def sol1(self, nums: List[int]) -> List[int]:
        '''
        This solution requires two additional arrays which hold leftward and rightward multiplication results.
        '''
        L = len(nums)
        le, re = [1]*L, [1]*L
        for i in range(1,L):
            le[i] = le[i-1]*nums[i-1]
            re[L-i-1] = re[L-i]*nums[L-i]
        for i in range(L):
            le[i]*=re[i]
        return le
    
    def sol2(self, nums: List[int]) -> List[int]:
        '''
        This answer is the same as sol1 but much more space and time efficient
        '''
        ans, suf, pre = [1]*len(nums), 1, 1
        for i in range(len(nums)):
            ans[i] *= pre
            pre *= nums[i]
            ans[-1-i] *= suf
            suf *= nums[-1-i]
        return ans

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1, self.sol2]:
            self.assertEqual(sol([1,2,3,4]), [24,12,8,6])
            self.assertEqual(sol([-1,1,0,-3,3]), [0,0,9,0,0])

if __name__ == "__main__":
    unittest.main()
