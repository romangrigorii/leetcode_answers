import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    39: https://leetcode.com/problems/combination-sum/description/
    Given an array of distinct integers candidates and a target integer target, return a list of all unique 
    combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
    The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency
    of at least one of the chosen numbers is different.
    The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
    '''
    def sol1(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        def combsum(nums_left, num_sofar, target):
            if target < 0: return
            if target == 0: 
                out.append(num_sofar)
                return
            for i in range(len(nums_left)):
                combsum(nums_left[i:], num_sofar + [nums_left[i]], target - nums_left[i])
        combsum(candidates, [], target)
        return out
   
class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        for sol in [self.sol1]:
            self.assertEqual(sol(candidates=[2,3,6,7], target=7), [[2,2,3],[7]])
            self.assertEqual(sol(candidates=[2,3,5], target=8), [[2,2,2,2],[2,3,3],[3,5]])

if __name__ == "__main__":
    unittest.main()
