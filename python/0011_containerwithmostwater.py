import unittest
from typing import Optional, List
from helpers import *

class _ (Helpers):
    '''
    3:55
    11: https://leetcode.com/problems/container-with-most-water/
    Given an array of integers which constitue wall heights, find the largest volume of water which can be trapped within those walls.
    '''
    def sol1(self, height: List[int]) -> int:
        '''
        This solution keeps track of the max volume as it iterates through the array from both
        the left and the right, depending on which wall is smaller than the other.
        '''
        left=0
        right=len(height)-1
        ans=0
        while left<right:
            mi=min(height[left],height[right])*(right-left)
            ans=max(ans,mi)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return ans
    
class test(unittest.TestCase, _):
    def test_(self):
        self.assertEqual(self.sol1(height = [1,8,6,2,5,4,8,3,7]), 49)
        self.assertEqual(self.sol1(height = [1,1]), 1)

if __name__ == "__main__":
    unittest.main()