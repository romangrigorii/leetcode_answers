import unittest
from typing import Optional, List
import sys
sys.path.insert(0, "..")
sys.path.insert(0, "../..")
from helpers import *
import numpy as np
class _ (Helpers):
    '''
    1: You are given n dollars every morning by your parents. 
    An icecream truck comes by in the afternoon, selling your favorite icecream cone. 
    The price of the cone varies day to day and is represented by nums. 
    Find the maximum number of cones you could have bought by the end of last day. 
    '''
    def sol1(self, nums: List[int], n: int) -> List[int]:
        solution_space = [(0,0)] # ice_creams, money
        for i, num in enumerate(nums):
            new_solution_space = []
            for s in solution_space:
                new_solution_space.append((s[0],s[1]+n))
                if s[1]+n-num >= 0:
                    new_solution_space.append((s[0]+1,s[1]+n-num))
            max_ice = max(new_solution_space, key = lambda x: x[0])[0]
            max_money = max(new_solution_space, key = lambda x: x[1])[1]
            best_ice_sol = [q for q in new_solution_space if q[0]==max_ice]
            best_mon_sol = [q for q in new_solution_space if q[1]==max_money]
            best_ice_sol.sort(key = lambda x: x[1])
            best_mon_sol.sort(key = lambda x: x[0])
            solution_space = [best_ice_sol[-1], best_mon_sol[-1]]
        return solution_space[0][0]

class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        for sol in [self.sol1]:
            self.assertEqual(sol(nums = [1,3,2,4,1], n = 1), 3)
            self.assertEqual(sol(nums = [1,3,2,4,1], n = 2), 4)
            self.assertEqual(sol(nums = [1,3,2,4,1], n = 3), 5)

unittest.main()