import unittest
from typing import Optional, List

class _ :
    '''
    41: https://leetcode.com/problems/first-missing-positive/description/
    Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
    You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
    '''
    def sol1(self, nums: List[int]) -> int:        
        nums.append(0)
        n = len(nums)
        for i in range(n):
            if nums[i]<0 or nums[i]>=n:
                nums[i] = 0
        for i in range(n):
            nums[nums[i]%n] += n # this effectively turns the list into a counter -> the value is stored in index, and the count in number of n
        for i in range(n):
            if int(nums[i]/n) == 0:
                return i
        return n


    def sol2(self, nums: List[int]) -> int:
        nums=set(nums)
        i = 1
        while i:
            if i not in nums:
                return i
            i+=1    
    
    def sol3(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            while 0<nums[i]<=n and nums[nums[i]-1]!=nums[i]:
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1

class test(unittest.TestCase, _ ):
    def test_(self):
        for sol in [self.sol1, self.sol2, self.sol3]:
            self.assertEqual(sol([1,2,0]), 3)
            self.assertEqual(sol([-100,100,200]), 1)
            self.assertEqual(sol([3,4,-1,1]), 2)
            self.assertEqual(sol([7,8,9,11,12]), 1)
    

if __name__ == "__main__":
    unittest.main()
