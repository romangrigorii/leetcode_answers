import unittest
from typing import Optional, List
from helpers import *

class _(Helpers):
    '''
    123: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    Find the maximum profit you can achieve. You may complete at most two transactions.
    Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
    
    Approach 1: Dynamic Programming with State Machine
    - Track 4 states: buy1, sell1, buy2, sell2
    - For each price, update each state optimally
    - Time: O(n), Space: O(1)
    
    Approach 2: Divide and Conquer
    - For each day, calculate max profit from left and right
    - Combine left and right profits
    - Time: O(n), Space: O(n)
    '''
        
    def maxProfit(self, prices: List[int]) -> int:
        """
        Approach 1: State Machine DP
        Track 4 states: first buy, first sell, second buy, second sell
        For each price, we can either:
        - Buy first time (if haven't bought yet)
        - Sell first time (if have bought)
        - Buy second time (if have sold first time)
        - Sell second time (if have bought second time)
        """
        if not prices:
            return 0
            
        # Initialize states
        buy1 = buy2 = float('inf')  # Cost to buy (we want to minimize this)
        sell1 = sell2 = 0           # Profit from selling (we want to maximize this)
        
        for price in prices:
            # First transaction
            buy1 = min(buy1, price)                    # Buy at lowest price
            sell1 = max(sell1, price - buy1)           # Sell at highest profit
            
            # Second transaction
            buy2 = min(buy2, price - sell1)            # Buy using profit from first sale
            sell2 = max(sell2, price - buy2)           # Sell for maximum total profit
            
        return sell2
    
    def maxProfit_divide_conquer(self, prices: List[int]) -> int:
        """
        Approach 2: Divide and Conquer
        For each day, calculate max profit from left and right
        Then find the best combination
        """
        if not prices:
            return 0
            
        n = len(prices)
        
        # Calculate max profit from left to right
        left_profits = [0] * n
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            left_profits[i] = max(left_profits[i-1], prices[i] - min_price)
        
        # Calculate max profit from right to left
        right_profits = [0] * n
        max_price = prices[n-1]
        for i in range(n-2, -1, -1):
            max_price = max(max_price, prices[i])
            right_profits[i] = max(right_profits[i+1], max_price - prices[i])
        
        # Find best combination
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, left_profits[i] + right_profits[i])
        
        return max_profit
    
    def maxProfit_naive(self, prices: List[int]) -> int:
        """
        Approach 3: Naive approach (for comparison)
        Try all possible combinations of two transactions
        Time: O(n^2), Space: O(1)
        """
        if not prices:
            return 0
            
        n = len(prices)
        max_profit = 0
        
        # Try all possible combinations of two transactions
        for i in range(n):
            # First transaction: buy at i, sell at j
            for j in range(i+1, n):
                profit1 = prices[j] - prices[i]
                if profit1 <= 0:
                    continue
                    
                # Second transaction: buy at k, sell at l
                for k in range(j+1, n):
                    for l in range(k+1, n):
                        profit2 = prices[l] - prices[k]
                        if profit2 > 0:
                            max_profit = max(max_profit, profit1 + profit2)
        
        return max_profit

class test(unittest.TestCase, _, Helpers):
    def test_basic_cases(self):
        """Test basic cases"""
        for sol in [self.maxProfit, self.maxProfit_divide_conquer]:
            # Test case 1: [3,3,5,0,0,3,1,4] -> 6
            # Buy at 3, sell at 5 (profit 2), buy at 0, sell at 4 (profit 4) = 6
            self.assertEqual(sol([3,3,5,0,0,3,1,4]), 6)
            
            # Test case 2: [1,2,3,4,5] -> 4
            # Buy at 1, sell at 5 = 4 (only one transaction needed)
            self.assertEqual(sol([1,2,3,4,5]), 4)
    
    def test_edge_cases(self):
        """Test edge cases"""
        for sol in [self.maxProfit, self.maxProfit_divide_conquer]:
            # Empty array
            self.assertEqual(sol([]), 0)
            
            # Single element
            self.assertEqual(sol([1]), 0)
            
            # Two elements - no profit
            self.assertEqual(sol([5, 3]), 0)
            
            # Two elements - profit
            self.assertEqual(sol([3, 5]), 2)
    
    def test_decreasing_prices(self):
        """Test when prices are decreasing"""
        for sol in [self.maxProfit, self.maxProfit_divide_conquer]:
            self.assertEqual(sol([5, 4, 3, 2, 1]), 0)
            self.assertEqual(sol([10, 8, 6, 4, 2]), 0)
    
    def test_increasing_prices(self):
        """Test when prices are increasing"""
        for sol in [self.maxProfit, self.maxProfit_divide_conquer]:
            # Single transaction is optimal
            self.assertEqual(sol([1, 2, 3, 4, 5]), 4)
            self.assertEqual(sol([1, 3, 5, 7, 9]), 8)
    
    def test_two_transactions_optimal(self):
        """Test cases where two transactions give better profit"""
        for sol in [self.maxProfit, self.maxProfit_divide_conquer]:
            # [1, 5, 2, 8] -> Buy at 1, sell at 5 (4), buy at 2, sell at 8 (6) = 10
            self.assertEqual(sol([1, 5, 2, 8]), 10)
            
            # [3, 2, 6, 5, 0, 3] -> Buy at 2, sell at 6 (4), buy at 0, sell at 3 (3) = 7
            self.assertEqual(sol([3, 2, 6, 5, 0, 3]), 7)
            
            # [2, 1, 4, 5, 2, 9, 7] -> Buy at 1, sell at 5 (4), buy at 2, sell at 9 (7) = 11
            self.assertEqual(sol([2, 1, 4, 5, 2, 9, 7]), 11)
    
    def test_complex_cases(self):
        """Test more complex scenarios"""
        for sol in [self.maxProfit, self.maxProfit_divide_conquer]:
            # Multiple peaks and valleys
            self.assertEqual(sol([1, 4, 2, 7, 3, 9, 1, 6]), 13)
            
            # Alternating pattern
            self.assertEqual(sol([1, 3, 1, 3, 1, 3]), 4)
            
            # Large numbers
            self.assertEqual(sol([100, 200, 50, 300, 25, 400]), 625)
    
    def test_leetcode_examples(self):
        """Test official LeetCode examples"""
        for sol in [self.maxProfit, self.maxProfit_divide_conquer]:
            # Example 1: [3,3,5,0,0,3,1,4]
            self.assertEqual(sol([3,3,5,0,0,3,1,4]), 6)
            
            # Example 2: [1,2,3,4,5]
            self.assertEqual(sol([1,2,3,4,5]), 4)
            
            # Example 3: [7,6,4,3,1]
            self.assertEqual(sol([7,6,4,3,1]), 0)
    
    def test_performance_comparison(self):
        """Compare performance of different approaches"""
        prices = [3,3,5,0,0,3,1,4]
        
        # All approaches should give same result
        result1 = self.maxProfit(prices)
        result2 = self.maxProfit_divide_conquer(prices)
        result3 = self.maxProfit_naive(prices)
        
        self.assertEqual(result1, result2)
        self.assertEqual(result2, result3)
        self.assertEqual(result1, 6)
    
    def test_large_inputs(self):
        """Test with larger inputs"""
        for sol in [self.maxProfit, self.maxProfit_divide_conquer]:
            # Large array with pattern
            large_prices = [i % 10 for i in range(1000)]
            result = sol(large_prices)
            self.assertGreaterEqual(result, 0)
            
            # All same prices
            same_prices = [5] * 100
            self.assertEqual(sol(same_prices), 0)

if __name__ == "__main__":
    unittest.main()
