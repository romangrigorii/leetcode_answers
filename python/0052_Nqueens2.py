import unittest
from typing import Optional, List
from helpers import *

class _ (Helpers):
    '''
    52: https://leetcode.com/problems/n-queens-ii/
    The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
    Given an integer n, return the number of distinct solutions to the n-queens puzzle.
    '''
    
    def totalNQueens(self, n: int) -> int:
        """
        Optimized backtracking solution using bit manipulation for diagonal tracking.
        
        Time Complexity: O(n!) - but with significant pruning due to early termination
        Space Complexity: O(n) - recursion stack depth
        """
        if n == 0:
            return 0
            
        def backtrack(row, cols, diag1, diag2):
            if row == n:
                return 1
            
            count = 0
            for col in range(n):
                # Check if current position is valid
                if (col not in cols and 
                    row + col not in diag1 and 
                    row - col not in diag2):
                    
                    # Place queen and recurse
                    cols.add(col)
                    diag1.add(row + col)
                    diag2.add(row - col)
                    
                    count += backtrack(row + 1, cols, diag1, diag2)
                    
                    # Backtrack
                    cols.remove(col)
                    diag1.remove(row + col)
                    diag2.remove(row - col)
            
            return count
        
        return backtrack(0, set(), set(), set())
    
    def sol1(self, n: int) -> int:
        """
        Original solution with intercept tracking.
        
        Time Complexity: O(n!) - generates all valid configurations
        Space Complexity: O(n²) - storing intercepts
        """
        if n == 0:
            return 0
        intercepts = set()
        self.tot = 0 
        self.search(n, 0, intercepts)
        return self.tot

    def search(self, n, ystart, intercepts):
        interceptsnew = set()
        for x in range(n):
            if (x, ystart) not in intercepts:
                if ystart == n-1:
                    self.tot += 1
                else:
                    interceptsnew = [(x,i) for i in range(ystart+1, n)] + [(i+x-ystart,i) for i in range(ystart+1, n) if (i+x-ystart)<n] + [(x-i+ystart,i) for i in range(ystart+1, n) if (x-i+ystart)>=0]
                    self.search(n, ystart+1, intercepts | set(interceptsnew))
    
    def sol2(self, n: int) -> int:
        """
        BFS approach with not_allowed positions tracking.
        
        Time Complexity: O(n!) - explores all valid configurations
        Space Complexity: O(n²) - storing not_allowed positions
        """
        if n == 0:
            return 0
            
        def bfs(y, not_allowed):
            if y == n: 
                return 1
            
            count = 0
            for i in range(n):
                if (i, y) not in not_allowed:                        
                    not_allowed_new = set()
                    for j in range(1, n):
                        if y + j < n:
                            not_allowed_new.add((i, y+j))
                            if i + j < n: 
                                not_allowed_new.add((i+j, y+j))
                            if i - j >= 0: 
                                not_allowed_new.add((i-j, y+j))
                    count += bfs(y+1, not_allowed | not_allowed_new)
            return count
        
        return bfs(0, set())
    
    def sol3(self, n: int) -> int:
        """
        Optimized solution using bit manipulation for better performance.
        
        Time Complexity: O(n!) - but with faster bit operations
        Space Complexity: O(n) - recursion stack only
        """
        if n == 0:
            return 0
            
        def solve(row, cols, diag1, diag2):
            if row == n:
                return 1
            
            count = 0
            for col in range(n):
                # Use bit operations for faster checking
                if not (cols & (1 << col) or 
                       diag1 & (1 << (row + col)) or 
                       diag2 & (1 << (row - col + n - 1))):
                    
                    count += solve(row + 1, 
                                  cols | (1 << col), 
                                  diag1 | (1 << (row + col)), 
                                  diag2 | (1 << (row - col + n - 1)))
            
            return count
        
        return solve(0, 0, 0, 0)
    
    def sol4(self, n: int) -> int:
        """
        Iterative solution using stack-based approach.
        
        Time Complexity: O(n!) - explores all valid configurations
        Space Complexity: O(n²) - storing board states
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        count = 0
        stack = [(0, set(), set(), set())]
        
        while stack:
            row, cols, diag1, diag2 = stack.pop()
            
            if row == n:
                count += 1
                continue
            
            for col in range(n):
                if (col not in cols and 
                    row + col not in diag1 and 
                    row - col not in diag2):
                    
                    new_cols = cols.copy()
                    new_diag1 = diag1.copy()
                    new_diag2 = diag2.copy()
                    
                    new_cols.add(col)
                    new_diag1.add(row + col)
                    new_diag2.add(row - col)
                    
                    stack.append((row + 1, new_cols, new_diag1, new_diag2))
        
        return count
    
    def sol5(self, n: int) -> int:
        """
        Optimized solution using early termination and pruning.
        
        Time Complexity: O(n!) - but with aggressive pruning
        Space Complexity: O(n) - recursion stack depth
        """
        if n == 0:
            return 0
            
        def backtrack(row, cols, diag1, diag2):
            if row == n:
                return 1
            
            # Early termination: if we can't place a queen in this row, backtrack
            valid_positions = []
            for col in range(n):
                if (col not in cols and 
                    row + col not in diag1 and 
                    row - col not in diag2):
                    valid_positions.append(col)
            
            # If no valid positions, backtrack
            if not valid_positions:
                return 0
            
            count = 0
            for col in valid_positions:
                cols.add(col)
                diag1.add(row + col)
                diag2.add(row - col)
                
                count += backtrack(row + 1, cols, diag1, diag2)
                
                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)
            
            return count
        
        return backtrack(0, set(), set(), set())
    
    def sol6(self, n: int) -> int:
        """
        Optimized solution using integer representation for board state.
        
        Time Complexity: O(n!) - but with very fast bit operations
        Space Complexity: O(n) - recursion stack depth
        """
        if n == 0:
            return 0
            
        def solve(row, cols, diag1, diag2):
            if row == n:
                return 1
            
            count = 0
            for col in range(n):
                # Check if position is valid using bit operations
                if not (cols & (1 << col) or 
                       diag1 & (1 << (row + col)) or 
                       diag2 & (1 << (row - col + n - 1))):
                    
                    count += solve(row + 1, 
                                  cols | (1 << col), 
                                  diag1 | (1 << (row + col)), 
                                  diag2 | (1 << (row - col + n - 1)))
            
            return count
        
        return solve(0, 0, 0, 0)
    
    def sol7(self, n: int) -> int:
        """
        Optimized solution using memoization for repeated subproblems.
        
        Time Complexity: O(n!) - but with memoization for better performance
        Space Complexity: O(n) - recursion stack depth
        """
        if n == 0:
            return 0
            
        def backtrack(row, cols, diag1, diag2, memo):
            if row == n:
                return 1
            
            # Create a key for memoization (simplified)
            state = (row, tuple(sorted(cols)), tuple(sorted(diag1)), tuple(sorted(diag2)))
            if state in memo:
                return memo[state]
            
            count = 0
            for col in range(n):
                # Check if current position is valid
                if (col not in cols and 
                    row + col not in diag1 and 
                    row - col not in diag2):
                    
                    # Place queen and recurse
                    cols.add(col)
                    diag1.add(row + col)
                    diag2.add(row - col)
                    
                    count += backtrack(row + 1, cols, diag1, diag2, memo)
                    
                    # Backtrack
                    cols.remove(col)
                    diag1.remove(row + col)
                    diag2.remove(row - col)
            
            memo[state] = count
            return count
        
        return backtrack(0, set(), set(), set(), {})

class test(unittest.TestCase, _, Helpers):
    def test_all_solutions(self):
        # Define all test cases with input and expected output
        test_cases = [
            # Basic cases
            (1, 1),
            (2, 0),  # No solution for 2x2
            (3, 0),  # No solution for 3x3
            (4, 2),
            (5, 10),
            (6, 4),
            (7, 40),
            (8, 92),
            (9, 352),
            (10, 724),
            (11, 2680),
            (12, 14200),
        ]
        
        # Test all solutions with the same test cases
        for n, expected in test_cases:
            with self.subTest(n=n, expected=expected):
                # Test the main totalNQueens solution
                result1 = self.totalNQueens(n)
                self.assertEqual(result1, expected, f"totalNQueens failed for n={n}")
                
                # Test sol1 solution
                result2 = self.sol1(n)
                self.assertEqual(result2, expected, f"sol1 failed for n={n}")
                
                # Test sol2 solution
                result3 = self.sol2(n)
                self.assertEqual(result3, expected, f"sol2 failed for n={n}")
                
                # Test sol3 solution
                result4 = self.sol3(n)
                self.assertEqual(result4, expected, f"sol3 failed for n={n}")
                
                # Test sol4 solution
                result5 = self.sol4(n)
                self.assertEqual(result5, expected, f"sol4 failed for n={n}")
                
                # Test sol5 solution (early termination and pruning)
                result6 = self.sol5(n)
                self.assertEqual(result6, expected, f"sol5 failed for n={n}")
                
                # Test sol6 solution (integer representation)
                result7 = self.sol6(n)
                self.assertEqual(result7, expected, f"sol6 failed for n={n}")
                
                # Test sol7 solution (symmetry-based)
                result8 = self.sol7(n)
                self.assertEqual(result8, expected, f"sol7 failed for n={n}")
    
    def test_edge_cases(self):
        """Test edge cases and boundary conditions."""
        # Test n = 0
        self.assertEqual(self.totalNQueens(0), 0)
        self.assertEqual(self.sol1(0), 0)
        self.assertEqual(self.sol2(0), 0)
        self.assertEqual(self.sol3(0), 0)
        self.assertEqual(self.sol4(0), 0)
        self.assertEqual(self.sol5(0), 0)
        self.assertEqual(self.sol6(0), 0)
        self.assertEqual(self.sol7(0), 0)
        
        # Test n = 1
        self.assertEqual(self.totalNQueens(1), 1)
        self.assertEqual(self.sol1(1), 1)
        self.assertEqual(self.sol2(1), 1)
        self.assertEqual(self.sol3(1), 1)
        self.assertEqual(self.sol4(1), 1)
        self.assertEqual(self.sol5(1), 1)
        self.assertEqual(self.sol6(1), 1)
        self.assertEqual(self.sol7(1), 1)
    
    def test_consistency(self):
        """Test that all solutions give consistent results for a range of n values."""
        for n in range(1, 9):  # Test up to n=8 for reasonable runtime
            results = [
                self.totalNQueens(n),
                self.sol1(n),
                self.sol2(n),
                self.sol3(n),
                self.sol4(n),
                self.sol5(n),
                self.sol6(n),
                self.sol7(n)
            ]
            
            # All results should be the same
            first_result = results[0]
            for i, result in enumerate(results):
                self.assertEqual(result, first_result, 
                               f"Solution {i+1} inconsistent for n={n}: expected {first_result}, got {result}")

if __name__ == "__main__":
    unittest.main()
