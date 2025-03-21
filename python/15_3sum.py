import unittest
from typing import Optional, List
from helpers import *

class _ (Helpers):
    '''
    5:00
    15: https://leetcode.com/problems/3sum/
    Given an array of if integers, find all triplets which will sum to 0, where each of the triplets can not be the same value.
    i.e. [1, 1, -2] is invalid. 
    '''
    def sol1(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # we sort first so we can make sure we don't repeat triplets can can skip over repeating numbers
        L, result = len(nums), []
        for i in range(L):
            if i>0 and nums[i]==nums[i-1]: # skip over the repeating number
                continue
            target = -nums[i] # we set the target and now look for two more values which will add to the first number
            s, e = i+1, L-1 # note that we start from either end 
            while s<e:
                if nums[s]+nums[e] == target:
                    result.append([nums[i], nums[s], nums[e]])
                    s+=1
                    while s<e and nums[s] == nums[s-1]: # go through repeating values
                        s+=1
                elif nums[s] + nums[e] < target: # iterate over s and e around the value we need them to add up to
                    s+=1
                else:
                    e-=1
        return result
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):
        self.assertEqual(self.sol1(nums = [-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])
        self.assertEqual(self.sol1(nums = [0,1,1]), [])
        self.assertEqual(self.sol1(nums = [0,0,0]), [[0,0,0]])

class ThreeSumPractice:
    '''
    5:00
    15: https://leetcode.com/problems/3sum/
    Given an array of if integers, find all triplets which will sum to 0, where each of the triplets can not be the same value.
    i.e. [1, 1, -2] is invalid. 
    '''
    def sol1(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if not nums: return nums
        L, result = len(nums), []
        for i in range(L):
            if i>0 and nums[i-1] == nums[i]: continue # iterate while the number is the same
            target = -nums[i]
            l = i+1
            r = L-1
            while l<r:                
                if  nums[l] + nums[r] == target:
                    result.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[-1]: l+=1
                elif (nums[l] + nums[r]) < target: l+=1
                else: r-=1
        return result
    
class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        self.assertEqual(self.sol1(nums = [-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])
        self.assertEqual(self.sol1(nums = [0,1,1]), [])
        self.assertEqual(self.sol1(nums = [0,0,0]), [[0,0,0]])


if __name__ == "__main__":
    unittest.main()