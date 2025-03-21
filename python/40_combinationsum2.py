import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    40: https://leetcode.com/problems/combination-sum-ii/
    Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations
    is candidates where the candidate numbers sum to target. 
    Each number in candidates may only be used once in the combination.
    Note: The solution set must not contain duplicate combinations.
    '''
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        candidates.sort()
        self.dfs_dontrepeat(candidates, target, out, [])
        return out
    
    def dfs_dontrepeat(self, candidates, target, out, sofar):
        if target <0: return
        if target == 0: 
            out.append(sofar)
        for i, cand in enumerate(candidates):
            if i>0 and candidates[i] == candidates[i-1]:
                continue
            self.dfs_dontrepeat(candidates[i+1:], target - cand, out, sofar + [cand])

        
   

class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        self.assertEqual(self.combinationSum2(candidates=[10,1,2,7,6,1,5], target=8), [[1,1,6],[1,2,5],[1,7],[2,6]])
        self.assertEqual(self.combinationSum2(candidates=[2,5,2,1,2], target=5), [[1,2,2],[5]])

if __name__ == "__main__":
    unittest.main()
