import unittest
from typing import Optional, List
from helpers import *

class _ (Helpers):
    '''    
    2: https://leetcode.com/problems/add-two-numbers/
    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
    and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    '''
    def sol1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        out = ListNode()
        outout = out
        rem = 0
        while l1 or l2 or rem:
            out.next = ListNode()
            out = out.next
            newval = rem
            if l1:
                newval += l1.val
                l1 = l1.next
            if l2:
                newval += l2.val
                l2 = l2.next
            (newval, rem) = (newval - 10, 1) if newval>9 else (newval, 0)
            out.val = newval
        return outout.next
    def sol2(self, l1, l2):
        rem = 0
        res = ListNode()
        res_h = res
        while l1 or l2 or rem:
            res.next = ListNode()
            res = res.next
            if l1: 
                rem += l1.val
                l1 = l1.next
            if l2:
                rem += l2.val
                l2 = l2.next
            res.val = rem%10
            rem //= 10
        return res_h.next
    
class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        for sol in [self.sol1, self.sol2]:
            self.assertEqual(self.convb(sol(self.convf([2,4,3]), self.convf([5,6,4]))), [7,0,8])
            self.assertEqual(self.convb(sol(self.convf([0]), self.convf([0]))), [0])
            self.assertEqual(self.convb(sol(self.convf([9,9,9,9,9,9,9]), self.convf([9,9,9,9]))), [8,9,9,9,0,0,0,1])

if __name__ == "__main__":
    unittest.main()

# # #              Big-O analysis
# Time O(N)  : as the function will sweep through every element and add them
# Space O(N) : since we store the numbers in a new LL