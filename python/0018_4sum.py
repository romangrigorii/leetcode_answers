import unittest
from typing import Optional, List
from helpers import *

class _ (Helpers):
    '''
    18: https://leetcode.com/problems/4sum/description/
    Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target
    You may return the answer in any order.
    '''
    def sol1(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        out = []
        L = len(nums)
        if L <=3 : return out
        for ii in range(L):
            for jj in range(ii+1, L):
                targetn = target - nums[ii] - nums[jj]
                ll = jj + 1
                rr = L - 1
                while ll<rr:
                    if (nums[ll] + nums[rr]) < targetn:
                        ll += 1
                    elif (nums[ll] + nums[rr]) > targetn:
                        rr -=1
                    else:
                        out.append((nums[ii], nums[jj], nums[ll], nums[rr]))
                        ll+=1
                        rr-=1
        return [list(q) for q in set(out)]

    def sol2(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSum(left, right, nums: List[int], target: int, result, results):
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    results.append(result + [nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif s < target:
                    left += 1
                else:
                    right -= 1

        def findNsum(left, right, target, n, result, results):
            if right - left + 1 < n or n < 2 or target < nums[left] * n or target > nums[right] * n:
                return
            elif n == 2:
                twoSum(left, right, nums, target, result, results)
            else:
                for i in range(left, right + 1):
                    if i == left or (i > left and nums[i - 1] != nums[i]):
                        findNsum(i + 1, right, target - nums[i], n - 1, result + [nums[i]], results)

        nums.sort()
        results = []
        findNsum(0, len(nums)-1, target, 4, [], results)
        return results
    
    def sol3(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if i + 3 < n and nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break # there are no values left in nums which will satisfy the sum            
            # Early termination if the largest possible sum is less than target
            if i + 3 < n and nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                continue
            for j in range(i+1,n -2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                if j + 2 < n and nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break            
                # Early termination if the largest possible sum is less than target
                if j + 2 < n and nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                    continue
                k = j+1
                l = n - 1
                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if total < target:
                        k += 1
                    elif total > target:
                        l -= 1
                    else:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        while nums[k] == nums[k-1] and k < l:
                            k += 1
                        while nums[l] == nums[l-1] and k < l:
                            l -= 1
                        l -= 1
            return res

        
    
class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        for sol in (self.sol1, self.sol2, self.sol3):
            self.equal_lists(sol(nums = [1,0,-1,0,-2,2], target = 0), [[-2,-1,1,2],[-1,0,0,1], [-2,0,0,2]])
            self.equal_lists(sol(nums = [2,2,2,2,2], target = 8), [[2,2,2,2]])

if __name__ == "__main__":
    unittest.main()