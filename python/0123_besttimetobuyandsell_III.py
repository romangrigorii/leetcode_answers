import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    123: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    Find the maximum profit you can achieve. You may complete at most two transactions.
    Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
    '''
        
    def maxProfit(self, prices: List[int]) -> int:
        oneBuyOneSell = twoBuyTwoSell = 0
        oneBuy = twoBuy = float('inf')
        for i in range(len(prices)):
            price = prices[i]
            oneBuy = min(oneBuy, price) # we check if the one buy has been the optimal choice 
            oneBuyOneSell = max(oneBuyOneSell, price - oneBuy)
            twoBuy = min(twoBuy, price - oneBuyOneSell) # this is how we gurantee that the second purchase happens after the first is sold
            twoBuyTwoSell = max(twoBuyTwoSell, price - twoBuy)        
        return twoBuyTwoSell

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.maxProfit]:
            self.assertEqual(sol([3,3,5,0,0,3,1,4]), 6)
            self.assertEqual(sol([1,2,3,4,5]), 4)

if __name__ == "__main__":
    unittest.main()
