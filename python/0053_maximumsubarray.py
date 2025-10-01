import unittest
from typing import Optional, List
from helpers import *

class _ (Helpers):
    '''
    53: https://leetcode.com/problems/maximum-subarray
    Given an integer array nums, find the subarray with the largest sum, and return its sum.
    '''
    
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Optimized Kadane's algorithm implementation.
        
        Time Complexity: O(n) - single pass through the array
        Space Complexity: O(1) - constant extra space
        """
        if not nums:
            return 0
        
        max_sum = current_sum = nums[0]
        
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum
    
    def sol1(self, nums: List[int]) -> int:
        """
        Original Kadane's algorithm with in-place modification.
        
        Time Complexity: O(n) - single pass through the array
        Space Complexity: O(1) - modifies input array in-place
        """
        if not nums:
            return 0
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
    
    def sol2(self, nums: List[int]) -> int:
        """
        Kadane's algorithm with reset to zero for negative sums.
        
        Time Complexity: O(n) - single pass through the array
        Space Complexity: O(1) - constant extra space
        """
        if not nums:
            return 0
        total = 0
        ma = float('-inf')  # Handle all negative arrays
        for q in nums:
            total += q
            ma = max(ma, total)  # Update max before resetting
            if total < 0:
                total = 0
        return ma
    
    def sol3(self, nums: List[int]) -> int:
        """
        Divide and conquer approach.
        
        Time Complexity: O(n log n) - divide and conquer
        Space Complexity: O(log n) - recursion stack depth
        """
        if not nums:
            return 0
        def maxSubArrayHelper(left, right):
            if left > right:
                return 0
            if left == right:
                return nums[left]
            
            mid = (left + right) // 2
            
            # Find max subarray in left half
            left_max = maxSubArrayHelper(left, mid)
            
            # Find max subarray in right half
            right_max = maxSubArrayHelper(mid + 1, right)
            
            # Find max subarray crossing the middle
            left_sum = float('-inf')
            curr_sum = 0
            for i in range(mid, left - 1, -1):
                curr_sum += nums[i]
                left_sum = max(left_sum, curr_sum)
            
            right_sum = float('-inf')
            curr_sum = 0
            for i in range(mid + 1, right + 1):
                curr_sum += nums[i]
                right_sum = max(right_sum, curr_sum)
            
            cross_max = left_sum + right_sum
            
            return max(left_max, right_max, cross_max)
        
        return maxSubArrayHelper(0, len(nums) - 1)
    
    def sol4(self, nums: List[int]) -> int:
        """
        Dynamic programming approach with explicit DP array.
        
        Time Complexity: O(n) - single pass through the array
        Space Complexity: O(n) - DP array
        """
        if not nums:
            return 0
        
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
        
        return max(dp)
    
    def sol5(self, nums: List[int]) -> int:
        """
        Optimized DP approach with space optimization.
        
        Time Complexity: O(n) - single pass through the array
        Space Complexity: O(1) - constant extra space
        """
        if not nums:
            return 0
        
        max_sum = nums[0]
        curr_sum = nums[0]
        
        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
    
    def sol6(self, nums: List[int]) -> int:
        """
        Prefix sum approach.
        
        Time Complexity: O(n) - single pass through the array
        Space Complexity: O(1) - constant extra space
        """
        if not nums:
            return 0
        
        min_prefix = 0
        prefix_sum = 0
        max_sum = float('-inf')
        
        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - min_prefix)
            min_prefix = min(min_prefix, prefix_sum)
        
        return max_sum
    
    def sol7(self, nums: List[int]) -> int:
        """
        Greedy approach with sliding window concept.
        
        Time Complexity: O(n) - single pass through the array
        Space Complexity: O(1) - constant extra space
        """
        if not nums:
            return 0
        
        max_sum = float('-inf')
        window_sum = 0
        
        for num in nums:
            window_sum += num
            max_sum = max(max_sum, window_sum)
            
            # If window sum becomes negative, reset window
            if window_sum < 0:
                window_sum = 0
        
        return max_sum
    
    def sol8(self, nums: List[int]) -> int:
        """
        Brute force approach for comparison (not recommended for large arrays).
        
        Time Complexity: O(n²) - nested loops
        Space Complexity: O(1) - constant extra space
        """
        if not nums:
            return 0
        
        max_sum = float('-inf')
        n = len(nums)
        
        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                max_sum = max(max_sum, curr_sum)
        
        return max_sum

class test(unittest.TestCase, _, Helpers):
    def test_all_solutions(self):
        # Define all test cases with input and expected output
        test_cases = [
            # Basic cases
            ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
            ([1], 1),
            ([5, 4, -1, 7, 8], 23),
            
            # Edge cases
            ([], 0),
            ([1], 1),
            ([-1], -1),
            ([-2, -1], -1),
            ([0], 0),
            ([1, 2, 3, 4, 5], 15),
            ([-1, -2, -3, -4, -5], -1),
            
            # Mixed cases
            ([1, -1, 1, -1, 1], 1),
            ([1, -2, 3, -4, 5], 5),
            ([-1, 2, -3, 4, -5], 4),
            ([2, -1, 3, -2, 4], 6),
            
            # Large numbers
            ([1000000, -1000000, 1000000], 1000000),
            ([-1000000, 1000000, -1000000], 1000000),
            
            # All positive
            ([1, 2, 3, 4], 10),
            ([10, 20, 30, 40], 100),
            
            # All negative
            ([-1, -2, -3, -4], -1),
            ([-10, -20, -30, -40], -10),
            
            # Alternating
            ([1, -1, 1, -1, 1, -1], 1),
            ([-1, 1, -1, 1, -1, 1], 1),
            
            # Single element variations
            ([42], 42),
            ([0], 0),
            ([-42], -42),
            
            # Two elements
            ([1, 2], 3),
            ([2, 1], 3),
            ([1, -1], 1),
            ([-1, 1], 1),
            ([-1, -2], -1),
            
            # Three elements
            ([1, 2, 3], 6),
            ([3, 2, 1], 6),
            ([1, -2, 3], 3),
            ([-1, 2, -3], 2),
            ([-1, -2, -3], -1),
            
            # Complex cases
            ([2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
            ([1, 2, -1, -2, 3, 4, -5, 6], 8),
            ([-2, -3, 4, -1, -2, 1, 5, -3], 7),
            
            # Large arrays
            ([1] * 100, 100),  # All ones
            ([-1] * 100, -1),  # All negative ones
            ([1, -1] * 50, 1),  # Alternating 1, -1
        ]
        
        # Test all solutions with the same test cases
        for input_nums, expected in test_cases:
            with self.subTest(input_nums=input_nums, expected=expected):
                # Test the main maxSubArray solution
                result1 = self.maxSubArray(input_nums.copy())
                self.assertEqual(result1, expected, f"maxSubArray failed for {input_nums}")
                
                # Test sol1 solution (modifies input, so use copy)
                nums_copy = input_nums.copy()
                result2 = self.sol1(nums_copy)
                self.assertEqual(result2, expected, f"sol1 failed for {input_nums}")
                
                # Test sol2 solution
                result3 = self.sol2(input_nums.copy())
                self.assertEqual(result3, expected, f"sol2 failed for {input_nums}")
                
                # Test sol3 solution (divide and conquer)
                result4 = self.sol3(input_nums.copy())
                self.assertEqual(result4, expected, f"sol3 failed for {input_nums}")
                
                # Test sol4 solution (DP)
                result5 = self.sol4(input_nums.copy())
                self.assertEqual(result5, expected, f"sol4 failed for {input_nums}")
                
                # Test sol5 solution (optimized DP)
                result6 = self.sol5(input_nums.copy())
                self.assertEqual(result6, expected, f"sol5 failed for {input_nums}")
                
                # Test sol6 solution (prefix sum)
                result7 = self.sol6(input_nums.copy())
                self.assertEqual(result7, expected, f"sol6 failed for {input_nums}")
                
                # Test sol7 solution (greedy)
                result8 = self.sol7(input_nums.copy())
                self.assertEqual(result8, expected, f"sol7 failed for {input_nums}")
                
                # Test sol8 solution (brute force) - only for smaller arrays
                if len(input_nums) <= 20:  # Limit brute force to smaller arrays
                    result9 = self.sol8(input_nums.copy())
                    self.assertEqual(result9, expected, f"sol8 failed for {input_nums}")
    
    def test_edge_cases(self):
        """Test edge cases and boundary conditions."""
        # Test empty array
        self.assertEqual(self.maxSubArray([]), 0)
        self.assertEqual(self.sol2([]), 0)
        self.assertEqual(self.sol3([]), 0)
        self.assertEqual(self.sol4([]), 0)
        self.assertEqual(self.sol5([]), 0)
        self.assertEqual(self.sol6([]), 0)
        self.assertEqual(self.sol7([]), 0)
        self.assertEqual(self.sol8([]), 0)
        
        # Test single element
        self.assertEqual(self.maxSubArray([42]), 42)
        self.assertEqual(self.sol2([42]), 42)
        self.assertEqual(self.sol3([42]), 42)
        self.assertEqual(self.sol4([42]), 42)
        self.assertEqual(self.sol5([42]), 42)
        self.assertEqual(self.sol6([42]), 42)
        self.assertEqual(self.sol7([42]), 42)
        self.assertEqual(self.sol8([42]), 42)
        
        # Test all negative
        self.assertEqual(self.maxSubArray([-1, -2, -3]), -1)
        self.assertEqual(self.sol2([-1, -2, -3]), -1)
        self.assertEqual(self.sol3([-1, -2, -3]), -1)
        self.assertEqual(self.sol4([-1, -2, -3]), -1)
        self.assertEqual(self.sol5([-1, -2, -3]), -1)
        self.assertEqual(self.sol6([-1, -2, -3]), -1)
        self.assertEqual(self.sol7([-1, -2, -3]), -1)
        self.assertEqual(self.sol8([-1, -2, -3]), -1)
    
    def test_consistency(self):
        """Test that all solutions give consistent results for a range of test cases."""
        test_arrays = [
            [1, 2, 3, 4, 5],
            [-1, -2, -3, -4, -5],
            [1, -1, 1, -1, 1],
            [2, -1, 3, -2, 4],
            [1, 2, -1, -2, 3, 4, -5, 6],
            [1, 2, 3, -10, 4, 5, 6],
            [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        ]
        
        for nums in test_arrays:
            results = [
                self.maxSubArray(nums.copy()),
                self.sol2(nums.copy()),
                self.sol3(nums.copy()),
                self.sol4(nums.copy()),
                self.sol5(nums.copy()),
                self.sol6(nums.copy()),
                self.sol7(nums.copy()),
                self.sol8(nums.copy()) if len(nums) <= 20 else None
            ]
            
            # Filter out None values (brute force for large arrays)
            results = [r for r in results if r is not None]
            
            # All results should be the same
            first_result = results[0]
            for i, result in enumerate(results):
                self.assertEqual(result, first_result, 
                               f"Solution {i+1} inconsistent for {nums}: expected {first_result}, got {result}")
    
    def test_performance_edge_cases(self):
        """Test performance edge cases and large arrays."""
        # Test with large array of all positive numbers
        large_positive = [1] * 1000
        self.assertEqual(self.maxSubArray(large_positive), 1000)
        self.assertEqual(self.sol2(large_positive), 1000)
        self.assertEqual(self.sol5(large_positive), 1000)
        
        # Test with large array of all negative numbers
        large_negative = [-1] * 1000
        self.assertEqual(self.maxSubArray(large_negative), -1)
        self.assertEqual(self.sol2(large_negative), -1)
        self.assertEqual(self.sol5(large_negative), -1)
        
        # Test with alternating pattern
        alternating = [1, -1] * 500
        self.assertEqual(self.maxSubArray(alternating), 1)
        self.assertEqual(self.sol2(alternating), 1)
        self.assertEqual(self.sol5(alternating), 1)

if __name__ == "__main__":
    unittest.main()