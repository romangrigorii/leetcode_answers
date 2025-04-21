import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    70: https://leetcode.com/problems/climbing-stairs/
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    '''
    def climbStairs(self, n: int) -> int:
        ways = [0] + [1]*(n + 1)
        for q in range(n):
            # there are only two ways to get to a step - jump one step or jump two steps.
            ways[q+2] = ways[q+1]
            ways[q+2] += ways[q]
        return ways[-1]

    
class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.climbStairs]:
            self.assertEqual(sol(2),2)
            self.assertEqual(sol(3),3)


if __name__ == "__main__":
    unittest.main()
