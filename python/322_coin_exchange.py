import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    322. https://leetcode.com/problems/coin-change/description/
    You are given an integer array coins representing coins of different denominations and an integer 
    amount representing a total amount of money.    
    Return the fewest number of coins that you need to make up that amount. If that amount of money 
    cannot be made up by any combination of the coins, return -1.
    You may assume that you have an infinite number of each kind of coin.
    '''
    def sol1(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse = True)
        minimal_exchanges = {0: 0}       
        self.coin_exchange(coins, amount, minimal_exchanges)
        if minimal_exchanges.get(amount) < float(inf):
            return minimal_exchanges.get(amount)
        else:
            return -1

    def coin_exchange(self, coins, amount, me):
        if amount in me: return             
        min_c = float(inf) # minimal amonunt of exchanges
        coin_exchanges = min_c
        for q in coins:
            if (amount - q) >= 0:
                if q == amount:
                    coin_exchanges = 1
                else:
                    self.coin_exchange(coins, amount - q, me)
                    coin_exchanges = me[amount-q] + 1
                min_c = min(min_c, coin_exchanges)
        me[amount] = min_c

    def sol2(self, coins: List[int], amount: int) -> int:
        maxx = float('inf')
        exchanges = [0] + [maxx]*amount
        for n in range(1,amount+1):
            exchanges[n] = min([exchanges[n - c] if (n-c)>=0 else maxx for c in coins]) + 1
        return [exchanges[-1], -1][exchanges[-1] == maxx]

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1, self.sol2]:
            self.assertEqual(sol([1,2,5], 11), 3)
            self.assertEqual(sol([2], 3), -1)

if __name__ == "__main__":
    unittest.main()
