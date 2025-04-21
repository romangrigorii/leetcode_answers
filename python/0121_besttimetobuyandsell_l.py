import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    121: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    '''
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buyp = float('inf') 
        for p in prices:
            buyp = min(buyp, p)
            profit = max(profit, p - buyp)
        return profit
        
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.maxProfit]:
            self.assertEqual(sol([7,1,5,3,6,4]), 5)


if __name__ == "__main__":
    unittest.main()
