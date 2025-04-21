import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    42: https://leetcode.com/problems/trapping-rain-water/description/
    Given n non-negative integers representing an elevation map where the width of each bar is 1,
    compute how much water it can trap after raining.
    '''
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0]*n
        right = [0]*n
        left[0] = height[0]
        right[-1] = height[-1]
        vol = 0
        for i in range(1,n):
            left[i] = max(height[i],left[i-1])
        for i in range(n-2,-1,-1):
            right[i] = max(height[i],right[i+1])
        for i in range(n):
            vol += min(left[i],right[i])-height[i]
        return vol
    
    def trap2(self, height: List[int]) -> int:
        n=len(height)
        if not height or n < 3:
            return 0

        l, r = 0, n - 1
        L, R = height[l], height[r]
        res = 0
        while l < r:
            if L < R:
                l += 1
                L = max(L, height[l]) # the max height on the left so far - granted that the right side can support it
                res += L - height[l]
            else:
                r -= 1
                R = max(R, height[r])
                res += R - height[r]
        return res
   

class test(unittest.TestCase, _ ):
    def test_(self):
        self.assertEqual(self.trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6)
        self.assertEqual(self.trap([4,2,0,3,2,5]), 9)
    def test_2(self):
        self.assertEqual(self.trap2([0,1,0,2,1,0,1,3,2,1,2,1]), 6)
        self.assertEqual(self.trap2([4,2,0,3,2,5]), 9)
if __name__ == "__main__":
    unittest.main()
