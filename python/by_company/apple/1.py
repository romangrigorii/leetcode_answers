import sys
sys.path.insert(0, "..")
sys.path.insert(0, "../..")
import unittest
from typing import Optional, List
from helpers import *
import numpy as np

class _ (Helpers):
    '''
    1: 
    Given an integer n, return true if it's a power of two. otherwise return false 
    '''
    def sol1(self, n) -> bool:        
        return 2**int(log2(n))==n
        

class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        for sol in [self.sol1]:
            self.assertEqual(sol(2),True)
            self.assertEqual(sol(3),False)
            self.assertEqual(sol(8),True)
unittest.main()

# # #              Big-O analysis
# Time O(N)  : as the function will sweep through every element 
# Space O(N) : since at worst we will store N keys and their associated values 