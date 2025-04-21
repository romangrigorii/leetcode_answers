import unittest
from typing import Optional, List
from helpers import *
import math 

class _ :
    '''
    59: https://leetcode.com/problems/permutation-sequence/
    The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
    By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
    "123"
    "132"
    "213"
    "231"
    "312"
    "321"
    Given n and k, return the kth permutation sequence.
    '''
    def sol1(self, n: int, k: int) -> str:
        ans = ""
        nums = [i for i in range(1,n+1)] # n = 4 : 1 2 3 4
        for i in range(1,n+1):
            index = 0
            c = math.factorial(n-i) # c = 9 4 1 1
            while c < k: # for k == 9, this will be skipped, so we just take the first value -> 1
                index +=1
                k -= c                
            ans += str(nums[index])
            del nums[index] # if we take a number we delete it at the index
        return ans
    
    def sol2(self, n: int, k: int) -> str:
        ans = ""
        pos =[str(q) for q in list(range(1,n+1))]        
        while n>0:            
            n-=1
            tot = math.factorial(n)
            if tot<=1: k = 0
            ans += pos[k//tot]
            pos.remove(pos[k//tot])      
            k %= tot
        return ans

    
class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.sol2]:
            self.assertEqual(sol(3, 3), "213")
            self.assertEqual(sol(4, 9), "2314")
            self.assertEqual(sol(3, 1), "123")

if __name__ == "__main__":
    unittest.main()
    