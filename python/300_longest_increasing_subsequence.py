import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    300: https://leetcode.com/problems/longest-increasing-subsequence
    '''
    def sol1(self, nums: List[int]) -> int:
        '''
        This uses o(n^2) time cimplexity as it goes through every possible array that can be sub arrayed
        explanation : the index i goes through the array and sets the upper limit to which j can traverse.
        if we encounter a situation where index i holds a value greater than at  j, we check that the value
        thus far recorded at i is smaller than the one recorded at j. If it is, we set value at i to the one at j
        + 1. This sets the newest largest number we have reached when checking if nums[i]>nums[j] 
        '''
        n =  len(nums)
        dp = [1]*n # this holds number of longest subsequence thus far
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j] and dp[i]<(dp[j]+1):
                    dp[i] = dp[j]+1
        return max(dp)
    
    def sol2(self, nums: List[int]) -> int:
        if nums: li = [nums[0]] # we grab the first element of the array if avaialble else we return empty array
        else: return []
        for q in nums[1:]:            
            if q == li[-1]: # we pass if the element is the same as the last one in th array
                pass
            elif q > li[-1]: # we append if the array is larger than the previous 
                li.append(q)
            else: # if the new element is smaller than the last, we find its natural place in the array and place it there
                # this may seem counterintuitive, but the idea here is that we are not growing the array, we are just filling
                # it up in a ray that will create new opportunities for seeking out sequences
                for h in range(len(li)):
                    if li[h]>=q:
                        break
                li[h] = q
        return len(li)

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol([10,9,2,5,3,7,101,18]), 4)
            self.assertEqual(sol([0,1,0,3,2,3]), 4)
            self.assertEqual(sol([7,7,7,7,7,7,7]), 1)

if __name__ == "__main__":
    unittest.main()
