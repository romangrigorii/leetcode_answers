import unittest
from typing import List
from helpers import *

class Solution:
    '''
    39: https://leetcode.com/problems/combination-sum/description/
    Given an array of distinct integers candidates and a target integer target, return a list of all unique 
    combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
    The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency
    of at least one of the chosen numbers is different.
    The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
    '''
    
    def combinationSum_sol1(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach 1: Backtracking with pruning
        Time: O(n^(target/min_candidate)) - exponential but with pruning
        Space: O(target/min_candidate) - depth of recursion
        """
        def backtrack(start, current_sum, current_combination):
            if current_sum == target:
                result.append(current_combination[:])
                return
            
            for i in range(start, len(candidates)):
                # Pruning: if adding current candidate exceeds target, skip
                if current_sum + candidates[i] > target:
                    continue
                
                current_combination.append(candidates[i])
                # Use i (not i+1) because we can reuse the same element
                backtrack(i, current_sum + candidates[i], current_combination)
                current_combination.pop()
        
        result = []
        candidates.sort()  # Sort to enable pruning
        backtrack(0, 0, [])
        return result
    
    def combinationSum_sol2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach 2: DFS with early termination
        Time: O(n^(target/min_candidate))
        Space: O(target/min_candidate)
        """
        def dfs(index, remaining, path):
            if remaining == 0:
                result.append(path[:])
                return
            
            if index >= len(candidates) or remaining < 0:
                return
            
            # Include current candidate
            path.append(candidates[index])
            dfs(index, remaining - candidates[index], path)
            path.pop()
            
            # Skip current candidate
            dfs(index + 1, remaining, path)
        
        result = []
        candidates.sort()
        dfs(0, target, [])
        return result
    
    def combinationSum_sol3(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach 3: Iterative approach using stack
        Time: O(n^(target/min_candidate))
        Space: O(n^(target/min_candidate)) - to store all combinations
        """
        if not candidates:
            return []
        
        candidates.sort()
        result = []
        stack = [(0, target, [])]  # (start_index, remaining_target, current_combination)
        
        while stack:
            start, remaining, combination = stack.pop()
            
            if remaining == 0:
                result.append(combination)
                continue
            
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                
                new_combination = combination + [candidates[i]]
                stack.append((i, remaining - candidates[i], new_combination))
        
        return result
    
    def combinationSum_sol4(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach 4: Optimized backtracking with frequency counting
        Time: O(n^(target/min_candidate))
        Space: O(target/min_candidate)
        """
        def backtrack(start, remaining, combination):
            if remaining == 0:
                result.append(combination[:])
                return
            
            for i in range(start, len(candidates)):
                candidate = candidates[i]
                # Early termination if candidate is too large
                if candidate > remaining:
                    break
                
                # Calculate how many times we can use this candidate
                max_freq = remaining // candidate
                
                for freq in range(1, max_freq + 1):
                    combination.extend([candidate] * freq)
                    backtrack(i + 1, remaining - candidate * freq, combination)
                    # Remove the added elements
                    for _ in range(freq):
                        combination.pop()
        
        result = []
        candidates.sort()
        backtrack(0, target, [])
        return result


class TestCombinationSum(unittest.TestCase, Solution, Helpers):
    
    def setUp(self):
        self.solutions = [
            self.combinationSum_sol1,
            self.combinationSum_sol2,
            self.combinationSum_sol3,
            self.combinationSum_sol4
        ]
    
    def test_basic_cases(self):
        """Test basic cases from LeetCode examples"""
        test_cases = [
            ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
            ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ]
        
        for candidates, target, expected in test_cases:
            for i, solution in enumerate(self.solutions):
                with self.subTest(candidates=candidates, target=target, solution=f"sol{i+1}"):
                    result = solution(candidates, target)
                    # Sort both result and expected for comparison
                    result_sorted = sorted([sorted(combo) for combo in result])
                    expected_sorted = sorted([sorted(combo) for combo in expected])
                    self.assertEqual(result_sorted, expected_sorted,
                                   f"Failed for candidates={candidates}, target={target}, solution=sol{i+1}")
    
    def test_edge_cases(self):
        """Test edge cases"""
        test_cases = [
            ([], 5, []),                           # Empty candidates
            ([1], 1, [[1]]),                       # Single candidate, target found
            ([2], 1, []),                          # Single candidate, target not found
            ([1, 2], 0, [[]]),                     # Target is 0
            ([1, 2, 3], 1, [[1]]),                 # Target is minimum candidate
        ]
        
        for candidates, target, expected in test_cases:
            for i, solution in enumerate(self.solutions):
                with self.subTest(candidates=candidates, target=target, solution=f"sol{i+1}"):
                    result = solution(candidates, target)
                    result_sorted = sorted([sorted(combo) for combo in result])
                    expected_sorted = sorted([sorted(combo) for combo in expected])
                    self.assertEqual(result_sorted, expected_sorted,
                                   f"Failed for candidates={candidates}, target={target}, solution=sol{i+1}")
    
    def test_single_element_reuse(self):
        """Test cases where single element is reused multiple times"""
        test_cases = [
            ([1], 3, [[1, 1, 1]]),                # Single element used multiple times
            ([2], 6, [[2, 2, 2]]),                # Single element used multiple times
            ([3], 9, [[3, 3, 3]]),                # Single element used multiple times
        ]
        
        for candidates, target, expected in test_cases:
            for i, solution in enumerate(self.solutions):
                with self.subTest(candidates=candidates, target=target, solution=f"sol{i+1}"):
                    result = solution(candidates, target)
                    result_sorted = sorted([sorted(combo) for combo in result])
                    expected_sorted = sorted([sorted(combo) for combo in expected])
                    self.assertEqual(result_sorted, expected_sorted,
                                   f"Failed for candidates={candidates}, target={target}, solution=sol{i+1}")
    
    def test_no_solution(self):
        """Test cases where no solution exists"""
        test_cases = [
            ([2, 4, 6], 7, []),                   # No solution possible
            ([3, 5, 7], 2, []),                   # Target too small
            ([10, 20, 30], 15, []),               # Target not achievable
        ]
        
        for candidates, target, expected in test_cases:
            for i, solution in enumerate(self.solutions):
                with self.subTest(candidates=candidates, target=target, solution=f"sol{i+1}"):
                    result = solution(candidates, target)
                    self.assertEqual(result, expected,
                                   f"Failed for candidates={candidates}, target={target}, solution=sol{i+1}")
    
    def test_larger_targets(self):
        """Test with larger targets"""
        test_cases = [
            ([2, 3, 5], 10, [[2, 2, 2, 2, 2], [2, 2, 3, 3], [2, 3, 5], [5, 5]]),
            ([1, 2, 3], 4, [[1, 1, 1, 1], [1, 1, 2], [1, 3], [2, 2]]),
        ]
        
        for candidates, target, expected in test_cases:
            for i, solution in enumerate(self.solutions):
                with self.subTest(candidates=candidates, target=target, solution=f"sol{i+1}"):
                    result = solution(candidates, target)
                    result_sorted = sorted([sorted(combo) for combo in result])
                    expected_sorted = sorted([sorted(combo) for combo in expected])
                    self.assertEqual(result_sorted, expected_sorted,
                                   f"Failed for candidates={candidates}, target={target}, solution=sol{i+1}")
    
    def test_negative_numbers(self):
        """Test with negative numbers (though this might not be typical for this problem)"""
        test_cases = [
            ([-1, 1, 2], 0, [[]]),                # Target 0 with mixed candidates
            ([1, 2, 3], 0, [[]]),                 # Target 0 with positive candidates
        ]
        
        for candidates, target, expected in test_cases:
            for i, solution in enumerate(self.solutions):
                with self.subTest(candidates=candidates, target=target, solution=f"sol{i+1}"):
                    result = solution(candidates, target)
                    result_sorted = sorted([sorted(combo) for combo in result])
                    expected_sorted = sorted([sorted(combo) for combo in expected])
                    self.assertEqual(result_sorted, expected_sorted,
                                   f"Failed for candidates={candidates}, target={target}, solution=sol{i+1}")
    
    def test_duplicate_candidates(self):
        """Test with duplicate candidates (though problem states distinct integers)"""
        # Skip this test since the problem states candidates are distinct integers
        pass
    
    def test_performance_consistency(self):
        """Test that all solutions produce consistent results"""
        test_cases = [
            ([1, 2, 3], 4),
            ([2, 3, 5], 8),
            ([1, 2, 3, 4], 6),
        ]
        
        for candidates, target in test_cases:
            results = []
            for solution in self.solutions:
                result = solution(candidates, target)
                results.append(sorted([sorted(combo) for combo in result]))
            
            # All solutions should produce the same result
            first_result = results[0]
            for i, result in enumerate(results[1:], 1):
                self.assertEqual(result, first_result,
                               f"Inconsistent results for candidates={candidates}, target={target}, "
                               f"sol1={first_result}, sol{i+1}={result}")
    
    def test_large_inputs(self):
        """Test with larger inputs to check performance"""
        candidates = [1, 2, 3, 4, 5]
        target = 10
        
        for i, solution in enumerate(self.solutions):
            with self.subTest(solution=f"sol{i+1}"):
                result = solution(candidates, target)
                # Just check that we get a valid result (not empty and all combinations sum to target)
                self.assertGreater(len(result), 0, f"Solution {i+1} returned empty result")
                
                for combination in result:
                    self.assertEqual(sum(combination), target,
                                   f"Combination {combination} doesn't sum to {target}")
    
    def test_ascending_order_property(self):
        """Test that combinations are in ascending order (if sorted)"""
        candidates = [3, 2, 1, 5, 4]  # Unsorted
        target = 8
        
        for i, solution in enumerate(self.solutions):
            with self.subTest(solution=f"sol{i+1}"):
                result = solution(candidates, target)
                
                # Check that each combination sums to target
                for combination in result:
                    self.assertEqual(sum(combination), target,
                                   f"Combination {combination} doesn't sum to {target}")
                
                # Check that all combinations are unique
                combinations_set = set(tuple(sorted(combo)) for combo in result)
                self.assertEqual(len(combinations_set), len(result),
                               f"Duplicate combinations found in solution {i+1}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
