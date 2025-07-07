import unittest
from typing import Optional, List
from helpers import *

class _ (Helpers):
    '''
    31: https://leetcode.com/problems/next-permutation/description/
    A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
    For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]. 
    The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 
    More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, 
    then the next permutation of that array is the permutation that follows it in the sorted container. 
    If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).
    For example, the next permutation of arr = [1,2,3] is [1,3,2].
    Similarly, the next permutation of arr = [2,3,1] is [3,1,2]. 
    While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
    Given an array of integers nums, find the next permutation of nums.
    The replacement must be in place and use only constant extra memory..
    '''
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Find the next lexicographically greater permutation of nums.
        
        Algorithm:
        1. Find the first decreasing element from the right (a[i] < a[i+1])
        2. Find the first element greater than a[i] from the right
        3. Swap these two elements
        4. Reverse the subarray after position i
        
        Time Complexity: O(n)
        Space Complexity: O(1) - in-place modification
        """
        n = len(nums)
        if n <= 1:
            return
        
        # Step 1: Find the first decreasing element from the right
        # This is the element that can be increased to get the next permutation
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # If no decreasing element found, the array is in descending order
        # Reverse it to get the smallest permutation (ascending order)
        if i < 0:
            nums.reverse()
            return
        
        # Step 2: Find the first element greater than nums[i] from the right
        # This element will be swapped with nums[i] to get the next permutation
        j = n - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        
        # Step 3: Swap the two elements
        nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the subarray after position i
        # This ensures we get the smallest possible arrangement for the remaining elements
        left = i + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    
    def sol1(self, nums: List[int]):
        l = 0
        r = len(nums)-1
        while r>l:
            if nums[r]>nums[r-1]:
                i = r+1
                imin = r
                while i<len(nums):
                    if nums[i]>nums[r-1] and nums[i]<nums[imin]:
                        imin = i
                    i+=1
                nums[imin], nums[r-1] = nums[r-1], nums[imin]
                break
            else:
                r -= 1

        q = nums[r:]
        q.sort()
        nums[r:] = q      
        return nums
    
    def sol2(self, nums: List[int]):
        i = j = len(nums)-1
        # First we'll find the first non-increasing element starting from the end
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        # After completion of the first loop, there will be two cases
        # 1. Our i becomes zero (This will happen if the given array is sorted decreasingly). In this case, we'll simply reverse the sequence and will return 
        if i == 0:
            nums.reverse()
            return nums
        # 2. If it's not zero then we'll find the first number greater than nums[i-1] starting from end
        while nums[j] <= nums[i-1]:
            j -= 1
        # Now out pointer is pointing at two different positions
        # i. first non-assending number from end
        # j. first number greater than nums[i-1]
        
        # We'll swap these two numbers
        nums[i-1], nums[j] = nums[j], nums[i-1]
        
        # We'll reverse a sequence strating from i to end
        nums[i:]= nums[len(nums)-1:i-1:-1]
        # We don't need to return anything as we've modified nums in-place
        return nums
 
class test(unittest.TestCase, _, Helpers):
    def test_all_solutions(self):
        # Define all test cases with input and expected output
        test_cases = [
            ([1, 2, 3], [1, 3, 2]),           # Normal case
            ([3, 2, 1], [1, 2, 3]),           # Largest permutation -> smallest
            ([1, 1, 5], [1, 5, 1]),           # Duplicate elements
            ([1, 4, 3, 2], [2, 1, 3, 4]),     # More complex case
            ([1, 4, 5, 3, 2], [1, 5, 2, 3, 4]), # Another complex case
            ([1], [1]),                        # Single element
            ([2, 1], [1, 2]),                 # Two elements
            ([1, 2], [2, 1]),                 # Two elements ascending
            ([1, 3, 2], [2, 1, 3]),           # Three elements
            ([2, 3, 1], [3, 1, 2]),           # Three elements
            ([1, 2, 3, 4], [1, 2, 4, 3]),     # Four elements
            ([4, 3, 2, 1], [1, 2, 3, 4]),     # Four elements descending
            ([1, 1, 1], [1, 1, 1]),           # All same elements
            ([1, 2, 2], [2, 1, 2]),           # Duplicate elements
            ([2, 2, 1], [1, 2, 2]),           # Duplicate elements at end
        ]
        
        # Test all solutions with the same test cases
        for input_nums, expected in test_cases:
            with self.subTest(input_nums=input_nums, expected=expected):
                # Test the main nextPermutation solution
                nums1 = input_nums.copy()
                self.nextPermutation(nums1)
                self.assertEqual(nums1, expected, f"nextPermutation failed for {input_nums}")
                
                # Test sol1 solution
                nums2 = input_nums.copy()
                result2 = self.sol1(nums2)
                self.assertEqual(result2, expected, f"sol1 failed for {input_nums}")
                
                # Test sol2 solution
                nums3 = input_nums.copy()
                result3 = self.sol2(nums3)
                self.assertEqual(result3, expected, f"sol2 failed for {input_nums}")
    
if __name__ == "__main__":
    unittest.main()