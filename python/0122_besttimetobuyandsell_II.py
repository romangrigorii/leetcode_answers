import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    122: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
    You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
    On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. 
    However, you can buy it then immediately sell it on the same day. 
    Find and return the maximum profit you can achieve.
    '''
    def maxProfit(self, prices: List[int]) -> int:
        '''
        This works but is slow and doesnt pass LC tests
        '''        
        def helper(owned, day_number):
            if day_number >= len(prices): return 0
            if owned>=0:
                if (prices[day_number] - owned) >= 0: # we only sell we we make profit
                    res = max(prices[day_number] - owned + helper(-1,day_number+1), helper(owned,day_number+1)) # sell vs hold strategy
                else:
                    res = helper(owned,day_number+1)
            else:
                res = max(helper(-1,day_number+1), helper(prices[day_number], day_number+1)) # wait vs buy strategy
            return res
        return helper(-1, 0)
        
    def maxProfitDP(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1,len(prices)):
            q = prices[i]-prices[i-1]
            profit += (q>0)*q                
        return profit
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.maxProfit, self.maxProfitDP]:
            self.assertEqual(sol([7,1,5,3,6,4]), 7) # Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4. 
            # Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
            # Total profit is 4 + 3 = 7.
            self.assertEqual(sol([2,1,2,0,1]), 2)

if __name__ == "__main__":
    unittest.main()
