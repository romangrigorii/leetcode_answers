import unittest
from typing import Optional, List
from helpers import *

class _ (Helpers):
    '''
    3301: Maximize Total Unique Height of Towers
    Given a list of maximum heights for towers, select heights for each tower (<= maximum) 
    so that all heights are unique and maximize the total sum. If impossible, return -1.

    Your task is to assign a height to each tower so that:

    The height of the ith tower is a positive integer and does not exceed maximumHeight[i].
    No two towers have the same height.
    '''
    
    def maximizeSum(self, maximumHeight: List[int]) -> int:
        """
        Greedy solution: sort descending, always pick the largest possible unique height.
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """
        if not maximumHeight:
            return 0
        maximumHeight.sort(reverse=True)
        total = 0
        maxAllowed = float('inf')
        for h in maximumHeight:
            maxAllowed = min(maxAllowed - 1, h)
            if maxAllowed <= 0:
                return -1
            
            total += maxAllowed
        return total
    
    def sol1(self, maximumHeight: List[int]) -> int:
        """
        Original greedy solution (preserved, improved for clarity).
        """
        if not maximumHeight:
            return 0
        maximumHeight.sort(reverse=True)
        out = 0
        maxAllowed = float('inf')
        for h in maximumHeight:
            maxAllowed = min(maxAllowed - 1, h)
            if maxAllowed <= 0:
                return -1
            out += maxAllowed
        return out
    
    def sol2(self, maximumHeight: List[int]) -> int:
        """
        Greedy solution using a set to track used heights (less efficient, for comparison).
        """
        if not maximumHeight:
            return 0
        used = set()
        total = 0
        for h in sorted(maximumHeight, reverse=True):
            while h > 0 and h in used:
                h -= 1
            if h == 0:
                return -1
            used.add(h)
            total += h
        return total
    
    def sol3(self, maximumHeight: List[int]) -> int:
        """
        Greedy solution with heap (minimize repeated values).
        """
        import heapq
        if not maximumHeight:
            return 0
        hq = [-h for h in maximumHeight]
        heapq.heapify(hq)
        used = set()
        total = 0
        while hq:
            h = -heapq.heappop(hq)
            while h > 0 and h in used:
                h -= 1
            if h == 0:
                return -1
            used.add(h)
            total += h
        return total

class test(unittest.TestCase, _, Helpers):
    def test_all_solutions(self):
        # Define all test cases with input and expected output
        test_cases = [
            # Basic cases
            ([2, 2, 1], -1),  # Can only use heights 2,1 but need 3 towers
            ([2, 3, 4, 3], 10),  # Heights: 4,3,2,1 = 10
            ([1, 2, 3], 6),  # Heights: 3,2,1 = 6
            ([3, 2, 1], 6),  # Heights: 3,2,1 = 6
            ([1, 1, 1], -1),  # Can only use height 1 once, but need 3 towers
            ([5, 4, 3, 2, 1], 15),  # Heights: 5,4,3,2,1 = 15
            ([5, 5, 5, 5, 5], 15),  # Heights: 5,4,3,2,1 = 15
            ([5, 4, 4, 3, 2], 15),  # Heights: 5,4,3,2,1 = 15
            ([10, 9, 8, 7, 6], 40),  # Heights: 10,9,8,7,6 = 40
            ([1], 1),  # Height: 1 = 1
            ([100], 100),  # Height: 100 = 100
            ([2, 2], 3),  # Heights: 2,1 = 3
            ([2, 1], 3),  # Heights: 2,1 = 3
            ([2, 2, 2], -1),  # Can only use heights 2,1 but need 3 towers
            ([3, 2, 2, 1], -1),  # Heights: 3,2,1, but 4th tower can't use anything
            ([4, 3, 2, 1], 10),  # Heights: 4,3,2,1 = 10
            ([4, 4, 4, 4], 10),  # Heights: 4,3,2,1 = 10
            ([4, 3, 3, 2], 10),  # Heights: 4,3,2,1 = 10
            ([4, 3, 2, 2], 10),  # Heights: 4,3,2,1 = 10
            ([4, 3, 2, 1, 1], -1),  # Can only use heights 4,3,2,1 but need 5 towers
            ([1, 2, 2, 3, 3, 4], -1),  # Heights: 4,3,2,1, but 6th tower can't use anything
            ([1, 1, 2, 2, 3, 3], -1),  # Heights: 3,2,1, but 6th tower can't use anything
            ([1, 2, 3, 4, 5, 6], 21),  # Heights: 6,5,4,3,2,1 = 21
            ([6, 5, 4, 3, 2, 1], 21),  # Heights: 6,5,4,3,2,1 = 21
            ([10, 10, 10, 10, 10, 10, 10, 10, 10, 10], 55),  # Heights: 10,9,8,7,6,5,4,3,2,1 = 55
            ([1], 1),
            ([0], -1),  # Can't have height 0
            ([0, 0, 0], -1),  # Can't have height 0
            ([], 0),
        ]
        
        # Test all solutions with the same test cases
        for input_arr, expected in test_cases:
            with self.subTest(input_arr=input_arr, expected=expected):
                # Test the main maximizeSum solution
                result1 = self.maximizeSum(input_arr.copy())
                self.assertEqual(result1, expected, f"maximizeSum failed for {input_arr}")
                
                # Test sol1 solution
                result2 = self.sol1(input_arr.copy())
                self.assertEqual(result2, expected, f"sol1 failed for {input_arr}")
                
                # Test sol2 solution
                result3 = self.sol2(input_arr.copy())
                self.assertEqual(result3, expected, f"sol2 failed for {input_arr}")
                
                # Test sol3 solution
                result4 = self.sol3(input_arr.copy())
                self.assertEqual(result4, expected, f"sol3 failed for {input_arr}")
    
    def test_edge_cases(self):
        """Test edge cases and boundary conditions."""
        self.assertEqual(self.maximizeSum([]), 0)
        self.assertEqual(self.maximizeSum([0]), -1)
        self.assertEqual(self.maximizeSum([1]), 1)
        self.assertEqual(self.maximizeSum([2]), 2)
        self.assertEqual(self.maximizeSum([2, 2]), 3)
        self.assertEqual(self.maximizeSum([2, 2, 2]), -1)  # Can only use heights 2,1 but need 3 towers
        self.assertEqual(self.maximizeSum([1, 1, 1]), -1)
        self.assertEqual(self.maximizeSum([100]), 100)
        self.assertEqual(self.maximizeSum([100, 99, 98, 97, 96]), 490)
    
    def test_consistency(self):
        """Test that all solutions give consistent results for a range of test cases."""
        test_arrays = [
            [2, 2, 1],
            [2, 3, 4, 3],
            [1, 2, 3],
            [3, 2, 1],
            [1, 1, 1],
            [5, 4, 3, 2, 1],
            [5, 5, 5, 5, 5],
            [10, 9, 8, 7, 6],
            [1],
            [100],
            [2, 2],
            [2, 1],
            [2, 2, 2],
            [3, 2, 2, 1],
            [4, 3, 2, 1],
            [4, 4, 4, 4],
            [4, 3, 3, 2],
            [4, 3, 2, 2],
            [4, 3, 2, 1, 1],
            [1, 2, 2, 3, 3, 4],
            [1, 1, 2, 2, 3, 3],
            [1, 2, 3, 4, 5, 6],
            [6, 5, 4, 3, 2, 1],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [1],
            [0],
            [0, 0, 0],
            [],
        ]
        for arr in test_arrays:
            results = [
                self.maximizeSum(arr.copy()),
                self.sol1(arr.copy()),
                self.sol2(arr.copy()),
                self.sol3(arr.copy()),
            ]
            first_result = results[0]
            for i, result in enumerate(results):
                self.assertEqual(result, first_result, 
                               f"Solution {i+1} inconsistent for {arr}: expected {first_result}, got {result}")

if __name__ == "__main__":
    unittest.main()
