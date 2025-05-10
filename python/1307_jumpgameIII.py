import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    1306: https://leetcode.com/problems/jump-game-iii/description/
    Given an array of non-negative integers arr, you are initially positioned at start index of the array. 
    When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.
    Notice that you can not jump outside of the array at any time.
    '''
    def sol1(self, arr: List[int], start: int) -> bool:
        visited = set()
        stack = []
        stack.append(start)
        while stack:
            goto = stack.pop()
            if arr[goto] == 0 : return True
            visited.add(goto)
            if goto - arr[goto]>=0 and goto - arr[goto] not in visited:
                stack.append(goto - arr[goto])
            if goto + arr[goto]<len(arr) and goto + arr[goto] not in visited:
                stack.append(goto + arr[goto])
        return False

class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.sol1]:
            self.assertEqual(sol([4,2,3,0,3,1,2], 5), True)
            self.assertEqual(sol([4,2,3,0,3,1,2], 0), True)
            self.assertEqual(sol([3,0,2,1,2], 2), False)

if __name__ == "__main__":
    unittest.main()
