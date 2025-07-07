import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    33: https://leetcode.com/problems/search-in-rotated-sorted-array/ 
    Given a rotated sorted array, develop a O(log(n)) algorithm that will find the index of a target value
    '''
    
    def sol1(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while r>=l:
            m = int((l+r)/2)
            if nums[m] == target: return m
            if nums[r] == target: return r
            if nums[l] == target: return l
            if nums[m]>nums[l] and nums[m]>target and nums[l]<target: # if the left array is sorted, and target falls in between two ends, go there
                r = m-1
            else: # else we go to the right array
                l = l+1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        """
        Optimized binary search for rotated sorted array.
        
        Algorithm:
        1. Find the pivot point (where rotation occurs)
        2. Determine which half contains the target
        3. Perform binary search on the appropriate half
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        if not nums:
            return -1
        
        n = len(nums)
        left, right = 0, n - 1
        
        # Find the pivot (smallest element)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        pivot = left
        
        # Determine which half to search
        if pivot == 0:
            # Array is not rotated
            left, right = 0, n - 1
        elif target >= nums[0]:
            # Target is in the left half
            left, right = 0, pivot - 1
        else:
            # Target is in the right half
            left, right = pivot, n - 1
        
        # Binary search in the appropriate half
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    
    def searchOnePass(self, nums: List[int], target: int) -> int:
        """
        One-pass binary search solution.
        
        Algorithm:
        - Use binary search to find target while handling rotation
        - Compare mid with left to determine which half is sorted
        - Check if target falls in the sorted half
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        if not nums:
            return -1
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            
            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                # Left half is sorted
                if nums[left] <= target < nums[mid]:
                    # Target is in left half
                    right = mid - 1
                else:
                    # Target is in right half
                    left = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    # Target is in right half
                    left = mid + 1
                else:
                    # Target is in left half
                    right = mid - 1
        
        return -1
    
    def searchBruteForce(self, nums: List[int], target: int) -> int:
        """
        Brute force solution for comparison.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1
    
   
class test(unittest.TestCase, _, Helpers):
    def test_all_solutions(self):
        # Define all test cases with input and expected output
        test_cases = [
            # Basic cases
            ([4,5,6,7,0,1,2], 0, 4),           # Target in rotated part
            ([4,5,6,7,0,1,2], 3, -1),          # Target not found
            ([1], 0, -1),                       # Single element, target not found
            ([1], 1, 0),                        # Single element, target found
            
            # No rotation cases
            ([1,2,3,4,5], 3, 2),               # No rotation, target in middle
            ([1,2,3,4,5], 1, 0),               # No rotation, target at start
            ([1,2,3,4,5], 5, 4),               # No rotation, target at end
            ([1,2,3,4,5], 6, -1),              # No rotation, target not found
            
            # Rotation cases
            ([3,4,5,1,2], 1, 3),               # Rotation at middle
            ([3,4,5,1,2], 4, 1),               # Target in left half
            ([3,4,5,1,2], 2, 4),               # Target in right half
            ([3,4,5,1,2], 6, -1),              # Target not found
            
            # Edge cases with rotation
            ([2,1], 1, 1),                      # Two elements, rotated
            ([2,1], 2, 0),                      # Two elements, target at start
            ([2,1], 3, -1),                     # Two elements, target not found
            
            # Multiple rotations
            ([5,1,3], 3, 2),                   # Three elements, target at end
            ([5,1,3], 1, 1),                   # Three elements, target in middle
            ([5,1,3], 5, 0),                   # Three elements, target at start
            ([5,1,3], 2, -1),                  # Three elements, target not found
            
            # Duplicate elements
            ([1,1,1,1,1], 1, 0),               # All same elements, target found (any index is valid)
            ([1,1,1,1,1], 2, -1),              # All same elements, target not found
            
            # Large arrays
            ([4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,0,1,2,3], 0, 96),  # Large array, target in rotated part
            ([4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,0,1,2,3], 50, 46),  # Large array, target in left half
            
            # Special cases
            ([], 1, -1),                        # Empty array
            ([1,3], 2, -1),                     # Two elements, target between
            ([1,3], 0, -1),                     # Two elements, target less than min
            ([1,3], 4, -1),                     # Two elements, target greater than max
            
            # Rotation at different positions
            ([6,7,8,9,1,2,3,4,5], 1, 4),       # Rotation after 4 elements
            ([6,7,8,9,1,2,3,4,5], 9, 3),       # Target at rotation point
            ([6,7,8,9,1,2,3,4,5], 5, 8),       # Target at end
            ([6,7,8,9,1,2,3,4,5], 6, 0),       # Target at start
        ]
        
        # Test all solutions with the same test cases
        for nums, target, expected in test_cases:
            with self.subTest(nums=nums, target=target, expected=expected):
                # Test the optimized solution
                result1 = self.search(nums, target)
                if expected == -1:
                    self.assertEqual(result1, expected, 
                                    f"search failed for nums={nums}, target={target}")
                else:
                    # For duplicate elements, any valid index is acceptable
                    if len(set(nums)) == 1 and target in nums:
                        self.assertNotEqual(result1, -1, 
                                           f"search failed for nums={nums}, target={target}")
                        self.assertEqual(nums[result1], target, 
                                       f"search returned wrong value for nums={nums}, target={target}")
                    else:
                        self.assertEqual(result1, expected, 
                                       f"search failed for nums={nums}, target={target}")
                
                # Test the one-pass solution
                result2 = self.searchOnePass(nums, target)
                if expected == -1:
                    self.assertEqual(result2, expected, 
                                    f"searchOnePass failed for nums={nums}, target={target}")
                else:
                    # For duplicate elements, any valid index is acceptable
                    if len(set(nums)) == 1 and target in nums:
                        self.assertNotEqual(result2, -1, 
                                           f"searchOnePass failed for nums={nums}, target={target}")
                        self.assertEqual(nums[result2], target, 
                                       f"searchOnePass returned wrong value for nums={nums}, target={target}")
                    else:
                        self.assertEqual(result2, expected, 
                                       f"searchOnePass failed for nums={nums}, target={target}")
                
                # Test the brute force solution
                result3 = self.searchBruteForce(nums, target)
                if expected == -1:
                    self.assertEqual(result3, expected, 
                                    f"searchBruteForce failed for nums={nums}, target={target}")
                else:
                    # For duplicate elements, any valid index is acceptable
                    if len(set(nums)) == 1 and target in nums:
                        self.assertNotEqual(result3, -1, 
                                           f"searchBruteForce failed for nums={nums}, target={target}")
                        self.assertEqual(nums[result3], target, 
                                       f"searchBruteForce returned wrong value for nums={nums}, target={target}")
                    else:
                        self.assertEqual(result3, expected, 
                                       f"searchBruteForce failed for nums={nums}, target={target}")
                
                # Test the original solution
                result4 = self.sol1(nums, target)
                if expected == -1:
                    self.assertEqual(result4, expected, 
                                    f"sol1 failed for nums={nums}, target={target}")
                else:
                    # For duplicate elements, any valid index is acceptable
                    if len(set(nums)) == 1 and target in nums:
                        self.assertNotEqual(result4, -1, 
                                           f"sol1 failed for nums={nums}, target={target}")
                        self.assertEqual(nums[result4], target, 
                                       f"sol1 returned wrong value for nums={nums}, target={target}")
                    else:
                        self.assertEqual(result4, expected, 
                                       f"sol1 failed for nums={nums}, target={target}")
    
    def test_(self):
        self.assertEqual(self.sol1(nums = [4,5,6,7,0,1,2], target = 0), 4)
        self.assertEqual(self.sol1(nums = [4,5,6,7,0,1,2], target = 3), -1)
        self.assertEqual(self.sol1(nums = [1], target = 0), -1)

if __name__ == "__main__":
    unittest.main()