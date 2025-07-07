import unittest
from typing import Optional, List
from helpers import *

class _ (Helpers):
    '''
    46: https://leetcode.com/problems/permutations/description/
    Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
    '''
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Optimized backtracking solution with in-place swapping.
        
        Time Complexity: O(n!) - factorial time as we generate all permutations
        Space Complexity: O(n) - recursion stack depth
        """
        def backtrack(start):
            if start == len(nums):
                print(nums)
                result.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  # backtrack
        
        result = []
        backtrack(0)
        return result
    
    def sol1(self, nums: List[int]) -> List[List[int]]:
        """
        DFS backtracking solution with list slicing.
        
        Time Complexity: O(n! * n) - factorial time plus O(n) for slicing
        Space Complexity: O(n!) - storing all permutations
        """
        out = []
        self.dfs(out, nums, [])
        return out  
    
    def dfs(self, out, available, current):
        if not available: 
            out.append(current)
        else:
            for i in range(len(available)):
                self.dfs(out, available[:i] + available[i+1:], current + [available[i]])

    def sol2(self, nums: List[int]) -> List[List[int]]:
        """
        Recursive solution with insertion at all positions.
        
        Time Complexity: O(n! * n) - factorial time plus O(n) for list operations
        Space Complexity: O(n!) - storing all permutations
        """
        out = self.sol2_helper(nums)
        return out
    
    def sol2_helper(self, nums):
        if not nums: 
            return [[]]
        if nums:
            out = self.sol2_helper(nums[1:])
            return [q[:i] + [nums[0]] + q[i:] for q in out for i in range(len(q)+1)]
    
    def sol3(self, nums: List[int]) -> List[List[int]]:
        """
        DFS backtracking solution with list slicing.
        
        Time Complexity: O(n! * n) - factorial time plus O(n) for slicing
        Space Complexity: O(n!) - storing all permutations
        """
        out = []
        self.dfs(out, nums, [])
        return out
    
    def sol3(self, nums: List[int]) -> List[List[int]]:
        """
        Iterative solution using next permutation algorithm.
        
        Time Complexity: O(n! * n) - factorial time plus O(n) for each permutation
        Space Complexity: O(n!) - storing all permutations
        """
        if not nums:
            return [[]]
        
        # Sort to get the first permutation
        nums_sorted = sorted(nums)
        result = [nums_sorted[:]]
        
        # Generate next permutations until we can't
        while True:
            # Find next permutation
            i = len(nums_sorted) - 2
            while i >= 0 and nums_sorted[i] >= nums_sorted[i + 1]:
                i -= 1
            
            if i < 0:
                break
            
            j = len(nums_sorted) - 1
            while nums_sorted[j] <= nums_sorted[i]:
                j -= 1
            
            nums_sorted[i], nums_sorted[j] = nums_sorted[j], nums_sorted[i]
            
            # Reverse the suffix
            left, right = i + 1, len(nums_sorted) - 1
            while left < right:
                nums_sorted[left], nums_sorted[right] = nums_sorted[right], nums_sorted[left]
                left += 1
                right -= 1
            
            result.append(nums_sorted[:])
        
        return result
    
    def sol4(self, nums: List[int]) -> List[List[int]]:
        """
        Heap's algorithm for generating permutations.
        
        Time Complexity: O(n!) - optimal for generating all permutations
        Space Complexity: O(n) - only recursion stack, no extra storage
        """
        if not nums:
            return [[]]
        def heaps_algorithm(n):
            if n == 1:
                result.append(nums[:])
                return
            for i in range(n):
                heaps_algorithm(n - 1)
                if n % 2 == 1:
                    nums[0], nums[n - 1] = nums[n - 1], nums[0]
                else:
                    nums[i], nums[n - 1] = nums[n - 1], nums[i]
        result = []
        heaps_algorithm(len(nums))
        return result
    
    def sol5(self, nums: List[int]) -> List[List[int]]:
        """
        Iterative solution using stack-based approach.
        
        Time Complexity: O(n! * n) - factorial time plus O(n) for each permutation
        Space Complexity: O(n!) - storing all permutations
        """
        if not nums:
            return [[]]
        
        result = []
        stack = [([], nums[:])]  # (current_permutation, remaining_numbers)
        
        while stack:
            curr_perm, remaining = stack.pop()
            
            if not remaining:
                result.append(curr_perm)
            else:
                for i in range(len(remaining)):
                    new_perm = curr_perm + [remaining[i]]
                    new_remaining = remaining[:i] + remaining[i+1:]
                    stack.append((new_perm, new_remaining))
        
        return result

class test(unittest.TestCase, _, Helpers):
    def test_all_solutions(self):
        # Define all test cases with input and expected output
        test_cases = [
            # Basic cases
            ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
            # ([0, 1], [[0, 1], [1, 0]]),
            # ([1], [[1]]),
            
            # # Edge cases
            # ([], [[]]),
            # ([1, 2], [[1, 2], [2, 1]]),
            # ([1, 2, 3, 4], [[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2],
            #                [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1],
            #                [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1],
            #                [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]]),
            
            # # Larger arrays
            # ([1, 2, 3, 4, 5], None),  # Too many permutations to list, just check count
            # ([1, 2, 3, 4, 5, 6], None),  # Too many permutations to list, just check count
            
            # # Special cases
            # ([0, -1, 1], [[0, -1, 1], [0, 1, -1], [-1, 0, 1], [-1, 1, 0], [1, 0, -1], [1, -1, 0]]),
            # ([10, 20, 30], [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]),
            
            # # Single element variations
            # ([42], [[42]]),
            # ([0], [[0]]),
            # ([-1], [[-1]]),
        ]
        
        # Test all solutions with the same test cases
        for nums, expected in test_cases:
            with self.subTest(nums=nums, expected=expected):
                # For large arrays, just check the count of permutations
                if expected is None:
                    expected_count = self.factorial(len(nums))
                    
                    # Test the main permute solution
                    result1 = self.permute(nums.copy())
                    self.assertEqual(len(result1), expected_count, f"permute count failed for {nums}")
                    self.assertTrue(self.all_unique_permutations(result1), f"permute has duplicates for {nums}")
                    
                    # Test sol1 solution
                    result2 = self.sol1(nums.copy())
                    self.assertEqual(len(result2), expected_count, f"sol1 count failed for {nums}")
                    self.assertTrue(self.all_unique_permutations(result2), f"sol1 has duplicates for {nums}")
                    
                    # Test sol2 solution
                    result3 = self.sol2(nums.copy())
                    self.assertEqual(len(result3), expected_count, f"sol2 count failed for {nums}")
                    self.assertTrue(self.all_unique_permutations(result3), f"sol2 has duplicates for {nums}")
                    
                    # Test sol3 solution
                    result4 = self.sol3(nums.copy())
                    self.assertEqual(len(result4), expected_count, f"sol3 count failed for {nums}")
                    self.assertTrue(self.all_unique_permutations(result4), f"sol3 has duplicates for {nums}")
                    
                    # Test sol4 solution
                    result5 = self.sol4(nums.copy())
                    self.assertEqual(len(result5), expected_count, f"sol4 count failed for {nums}")
                    self.assertTrue(self.all_unique_permutations(result5), f"sol4 has duplicates for {nums}")
                    
                    # Test sol5 solution
                    result6 = self.sol5(nums.copy())
                    self.assertEqual(len(result6), expected_count, f"sol5 count failed for {nums}")
                    self.assertTrue(self.all_unique_permutations(result6), f"sol5 has duplicates for {nums}")
                else:
                    # Test the main permute solution
                    result1 = self.permute(nums.copy())
                    self.assertEqual(sorted(result1), sorted(expected), f"permute failed for {nums}")
                    
                    # Test sol1 solution
                    result2 = self.sol1(nums.copy())
                    self.assertEqual(sorted(result2), sorted(expected), f"sol1 failed for {nums}")
                    
                    # Test sol2 solution
                    result3 = self.sol2(nums.copy())
                    self.assertEqual(sorted(result3), sorted(expected), f"sol2 failed for {nums}")
                    
                    # Test sol3 solution
                    result4 = self.sol3(nums.copy())
                    self.assertEqual(sorted(result4), sorted(expected), f"sol3 failed for {nums}")
                    
                    # Test sol4 solution
                    result5 = self.sol4(nums.copy())
                    self.assertEqual(sorted(result5), sorted(expected), f"sol4 failed for {nums}")
                    
                    # Test sol5 solution
                    result6 = self.sol5(nums.copy())
                    self.assertEqual(sorted(result6), sorted(expected), f"sol5 failed for {nums}")
    
    def factorial(self, n):
        """Calculate factorial of n."""
        if n <= 1:
            return 1
        return n * self.factorial(n - 1)
    
    def all_unique_permutations(self, perms):
        """Check if all permutations are unique."""
        return len(perms) == len(set(tuple(p) for p in perms))

if __name__ == "__main__":
    unittest.main()
