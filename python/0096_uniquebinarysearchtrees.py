import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    95: https://leetcode.com/problems/unique-binary-search-trees-ii/
    Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n 
    nodes of unique values from 1 to n. Return the answer in any order.
    '''
    def sol1(self, n: int) -> int:
        return factorial(2*n)//factorial(n)//factorial(n)//(n+1)
                
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol(1), 1)
            self.assertEqual(sol(2), 2)
            self.assertEqual(sol(3), 5)
            self.assertEqual(sol(4), 14)
            self.assertEqual(sol(5), 42)


if __name__ == "__main__":   
    unittest.main()
