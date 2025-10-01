import unittest
from typing import Optional, List
from helpers import *

class _ (Helpers):
    '''
    55: https://leetcode.com/problems/jump-game/
    You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents 
    your maximum jump length at that position.
    Return true if you can reach the last index, or false otherwise.
    '''
    
    def canJump(self, nums: List[int]) -> bool:
        """
        Optimized greedy approach - track the maximum reachable position.
        
        Time Complexity: O(n) - single pass through the array
        Space Complexity: O(1) - constant extra space
        """
        if not nums:
            return False
        
        max_reach = 0
        
        for i in range(len(nums)):
            # If current position is beyond what we can reach, return False
            if i > max_reach:
                return False
            
            # Update the maximum reachable position
            max_reach = max(max_reach, i + nums[i])
            
            # If we can reach the end, return True
            if max_reach >= len(nums) - 1:
                return True
        
        return max_reach >= len(nums) - 1
    
    def sol1(self, nums: List[int]) -> bool:
        """
        Improved dynamic programming approach with early termination.
        
        Time Complexity: O(n²) - but with early termination
        Space Complexity: O(n) - DP array
        """
        if not nums:
            return False
        
        n = len(nums)
        reachable = [False] * n
        reachable[0] = True
        
        for i in range(n):
            if not reachable[i]:
                return False
            
            # Early termination: if we can reach the end from current position
            if i + nums[i] >= n - 1:
                return True
            
            # Mark all reachable positions from current position
            for jump in range(1, min(nums[i] + 1, n - i)):
                reachable[i + jump] = True
        
        return reachable[-1]
    
    def sol2(self, nums: List[int]) -> bool:
        """
        Improved greedy approach with step counting.
        
        Time Complexity: O(n) - single pass through the array
        Space Complexity: O(1) - constant extra space
        """
        if not nums:
            return False
        
        steps = 0
        for i, num in enumerate(nums):
            if steps < 0:
                return False
            elif num > steps:
                steps = num
            steps -= 1
            
            # Early termination: if we can reach the end
            if i + steps >= len(nums) - 1:
                return True
        
        return True
    
    def sol3(self, nums: List[int]) -> bool:
        """
        Backward greedy approach - work backwards from the end.
        
        Time Complexity: O(n) - single pass through the array
        Space Complexity: O(1) - constant extra space
        """
        if not nums:
            return False
        
        destination = len(nums) - 1
        
        for i in range(destination - 1, -1, -1):
            if nums[i] + i >= destination:
                destination = i
        
        return destination == 0
    
    def sol4(self, nums: List[int]) -> bool:
        """
        Recursive approach with memorization.
        
        Time Complexity: O(n²) - but with memorization
        Space Complexity: O(n) - recursion stack and memorization
        """
        if not nums:
            return False
        
        memo = {}
        
        def canReachEnd(position):
            if position in memo:
                return memo[position]
            
            if position >= len(nums) - 1:
                return True
            
            if nums[position] == 0:
                return False
            
            for jump in range(1, nums[position] + 1):
                if canReachEnd(position + jump):
                    memo[position] = True
                    return True
            
            memo[position] = False
            return False
        
        return canReachEnd(0)
    
    def sol5(self, nums: List[int]) -> bool:
        """
        Iterative approach with stack-based DFS.
        
        Time Complexity: O(n²) - in worst case
        Space Complexity: O(n) - stack space
        """
        if not nums:
            return False
        
        n = len(nums)
        visited = set()
        stack = [0]
        
        while stack:
            position = stack.pop()
            
            if position >= n - 1:
                return True
            
            if position in visited:
                continue
            
            visited.add(position)
            
            # Try all possible jumps from current position
            for jump in range(1, nums[position] + 1):
                next_position = position + jump
                if next_position < n and next_position not in visited:
                    stack.append(next_position)
        
        return False
    
    def sol6(self, nums: List[int]) -> bool:
        """
        Optimized greedy approach with boundary checking.
        
        Time Complexity: O(n) - single pass through the array
        Space Complexity: O(1) - constant extra space
        """
        if not nums:
            return False
        
        n = len(nums)
        max_reach = 0
        
        for i in range(n):
            # If we can't reach current position, return False
            if i > max_reach:
                return False
            
            # Update max reach
            max_reach = max(max_reach, i + nums[i])
            
            # Early termination
            if max_reach >= n - 1:
                return True
        
        return max_reach >= n - 1
    
    def sol7(self, nums: List[int]) -> bool:
        """
        Two-pointer approach with sliding window concept.
        
        Time Complexity: O(n) - single pass through the array
        Space Complexity: O(1) - constant extra space
        """
        if not nums:
            return False
        
        n = len(nums)
        left = 0
        right = 0
        max_reach = 0
        
        while left <= right and right < n - 1:
            # Calculate the maximum reach from current window
            for i in range(left, right + 1):
                max_reach = max(max_reach, i + nums[i])
            
            # If we can't reach further, return False
            if max_reach <= right:
                return False
            
            # Move window
            left = right + 1
            right = max_reach
        
        return max_reach >= n - 1
    
    def sol8(self, nums: List[int]) -> bool:
        """
        Binary search approach on the minimum jumps needed.
        
        Time Complexity: O(n log n) - binary search with linear validation
        Space Complexity: O(1) - constant extra space
        """
        if not nums:
            return False
        
        n = len(nums)
        
        def canReachWithJumps(max_jumps):
            position = 0
            jumps_used = 0
            
            while position < n - 1 and jumps_used < max_jumps:
                if nums[position] == 0:
                    return False
                
                # Find the best next position
                best_next = position
                for jump in range(1, min(nums[position] + 1, n - position)):
                    next_pos = position + jump
                    if next_pos >= n - 1:
                        return True
                    if next_pos + nums[next_pos] > best_next + nums[best_next]:
                        best_next = next_pos
                
                position = best_next
                jumps_used += 1
            
            return position >= n - 1
        
        # Binary search on the number of jumps needed
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if canReachWithJumps(mid):
                right = mid
            else:
                left = mid + 1
        
        return left < n

class test(unittest.TestCase, _, Helpers):
    def test_all_solutions(self):
        # Define all test cases with input and expected output
        test_cases = [
            # Basic cases
            ([2, 3, 1, 1, 4], True),
            ([3, 2, 1, 0, 4], False),
            ([2, 0], True),
            ([1, 0, 1, 0], False),
            
            # Edge cases
            ([], False),
            ([0], True),
            ([1], True),
            ([2], True),
            ([0, 1], False),
            ([1, 0], True),
            ([2, 0, 0], True),
            
            # Single element variations
            ([0], True),
            ([1], True),
            ([5], True),
            
            # Two elements
            ([1, 0], True),
            ([0, 1], False),
            ([2, 0], True),
            ([1, 1], True),
            ([0, 0], False),
            
            # Three elements
            ([1, 1, 1], True),
            ([1, 0, 1], False),
            ([2, 0, 0], True),
            ([1, 2, 0], True),
            ([0, 1, 1], False),
            
            # Complex cases
            ([2, 3, 1, 1, 4], True),
            ([3, 2, 1, 0, 4], False),
            ([2, 3, 0, 1, 4], True),
            ([1, 3, 2], True),
            ([0, 3, 1], False),
            ([1, 2, 3, 4, 5], True),
            ([5, 4, 3, 2, 1], True),
            ([1, 1, 1, 1, 1], True),
            ([0, 0, 0, 0, 0], False),
            
            # Large jumps
            ([10, 0, 0, 0, 0], True),
            ([1, 0, 0, 0, 10], False),
            ([5, 0, 0, 0, 0, 0], True),
            
            # Alternating patterns
            ([1, 0, 1, 0, 1], False),
            ([2, 0, 2, 0, 2], True),
            ([1, 1, 0, 1, 1], False),
            
            # Boundary cases
            ([1, 0, 0, 0], False),
            ([2, 0, 0, 0], False),
            ([1, 1, 0, 0], False),
            ([1, 0, 1, 0], False),
            
            # Large arrays
            ([1] * 100, True),  # All ones
            ([0] * 100, False),  # All zeros
            ([100] + [0] * 99, True),  # Large first jump
            ([1] * 99 + [0], True),  # All ones except last
        ]
        
        # Test all solutions with the same test cases
        for input_nums, expected in test_cases:
            with self.subTest(input_nums=input_nums, expected=expected):
                # Test the main canJump solution
                result1 = self.canJump(input_nums.copy())
                self.assertEqual(result1, expected, f"canJump failed for {input_nums}")
                
                # Test sol1 solution
                result2 = self.sol1(input_nums.copy())
                self.assertEqual(result2, expected, f"sol1 failed for {input_nums}")
                
                # Test sol2 solution
                result3 = self.sol2(input_nums.copy())
                self.assertEqual(result3, expected, f"sol2 failed for {input_nums}")
                
                # Test sol3 solution
                result4 = self.sol3(input_nums.copy())
                self.assertEqual(result4, expected, f"sol3 failed for {input_nums}")
                
                # Test sol4 solution (recursive with memoization)
                result5 = self.sol4(input_nums.copy())
                self.assertEqual(result5, expected, f"sol4 failed for {input_nums}")
                
                # Test sol5 solution (iterative DFS)
                result6 = self.sol5(input_nums.copy())
                self.assertEqual(result6, expected, f"sol5 failed for {input_nums}")
                
                # Test sol6 solution (optimized greedy)
                result7 = self.sol6(input_nums.copy())
                self.assertEqual(result7, expected, f"sol6 failed for {input_nums}")
                
                # Test sol7 solution (two-pointer)
                result8 = self.sol7(input_nums.copy())
                self.assertEqual(result8, expected, f"sol7 failed for {input_nums}")
                
                # Test sol8 solution (binary search) - only for smaller arrays
                if len(input_nums) <= 20:  # Limit binary search to smaller arrays
                    result9 = self.sol8(input_nums.copy())
                    self.assertEqual(result9, expected, f"sol8 failed for {input_nums}")
    
    def test_edge_cases(self):
        """Test edge cases and boundary conditions."""
        # Test empty array
        self.assertEqual(self.canJump([]), False)
        self.assertEqual(self.sol1([]), False)
        self.assertEqual(self.sol2([]), False)
        self.assertEqual(self.sol3([]), False)
        self.assertEqual(self.sol4([]), False)
        self.assertEqual(self.sol5([]), False)
        self.assertEqual(self.sol6([]), False)
        self.assertEqual(self.sol7([]), False)
        
        # Test single element
        self.assertEqual(self.canJump([0]), True)
        self.assertEqual(self.sol1([0]), True)
        self.assertEqual(self.sol2([0]), True)
        self.assertEqual(self.sol3([0]), True)
        self.assertEqual(self.sol4([0]), True)
        self.assertEqual(self.sol5([0]), True)
        self.assertEqual(self.sol6([0]), True)
        self.assertEqual(self.sol7([0]), True)
        
        # Test all zeros
        self.assertEqual(self.canJump([0, 0, 0]), False)
        self.assertEqual(self.sol1([0, 0, 0]), False)
        self.assertEqual(self.sol2([0, 0, 0]), False)
        self.assertEqual(self.sol3([0, 0, 0]), False)
        self.assertEqual(self.sol4([0, 0, 0]), False)
        self.assertEqual(self.sol5([0, 0, 0]), False)
        self.assertEqual(self.sol6([0, 0, 0]), False)
        self.assertEqual(self.sol7([0, 0, 0]), False)
    
    def test_consistency(self):
        """Test that all solutions give consistent results for a range of test cases."""
        test_arrays = [
            [2, 3, 1, 1, 4],
            [3, 2, 1, 0, 4],
            [2, 0],
            [1, 0, 1, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [2, 0, 0, 0],
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
        ]
        
        for nums in test_arrays:
            results = [
                self.canJump(nums.copy()),
                self.sol1(nums.copy()),
                self.sol2(nums.copy()),
                self.sol3(nums.copy()),
                self.sol4(nums.copy()),
                self.sol5(nums.copy()),
                self.sol6(nums.copy()),
                self.sol7(nums.copy()),
                self.sol8(nums.copy()) if len(nums) <= 20 else None
            ]
            
            # Filter out None values (binary search for large arrays)
            results = [r for r in results if r is not None]
            
            # All results should be the same
            first_result = results[0]
            for i, result in enumerate(results):
                self.assertEqual(result, first_result, 
                               f"Solution {i+1} inconsistent for {nums}: expected {first_result}, got {result}")
    
    def test_performance_edge_cases(self):
        """Test performance edge cases and large arrays."""
        # Test with large array of all ones
        large_ones = [1] * 1000
        self.assertEqual(self.canJump(large_ones), True)
        self.assertEqual(self.sol2(large_ones), True)
        self.assertEqual(self.sol6(large_ones), True)
        
        # Test with large array of all zeros
        large_zeros = [0] * 1000
        self.assertEqual(self.canJump(large_zeros), False)
        self.assertEqual(self.sol2(large_zeros), False)
        self.assertEqual(self.sol6(large_zeros), False)
        
        # Test with large first jump
        large_jump = [1000] + [0] * 999
        self.assertEqual(self.canJump(large_jump), True)
        self.assertEqual(self.sol2(large_jump), True)
        self.assertEqual(self.sol6(large_jump), True)
        
        # Test with alternating pattern
        alternating = [1, 0] * 500
        self.assertEqual(self.canJump(alternating), False)
        self.assertEqual(self.sol2(alternating), False)
        self.assertEqual(self.sol6(alternating), False)

if __name__ == "__main__":
    unittest.main()
