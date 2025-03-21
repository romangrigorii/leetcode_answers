import unittest
from typing import Optional, List
from helpers import *
from collections import Counter

class _(Helpers) :
    '''
    86: https://leetcode.com/problems/partition-list/
    Given the head of a linked list and a value x, partition it such that all nodes less than x come 
    before nodes greater than or equal to x.
    You should preserve the original relative order of the nodes in each of the two partitions.
 
    '''
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        q1 = ListNode(-1, head) # tracks left half
        q2 = ListNode(-1, head) # tracks right half
        q1_h = q1 # keeps at head of left half
        q2_h = q2 # keeps at head of right half
        while q2.next:
            while q2.next and q2.next.next and q2.next.val >= x: # put it at the start of the queue
                q2 = q2.next
            if q2.next.val < x:                
                q1.next = q2.next
                q1 = q1.next
            if q2.next.val < x:
                q2.next = q2.next.next # skip
            else:
                q2 = q2.next # absorb
        q1.next = q2_h.next
        return q1_h.next
    
    def partition2(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)
        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l2.next = None
        l1.next = h2.next
        return h1.next

class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.partition, self.partition2]:
            self.assertEqual(self.convb(sol(self.convf([1,4,3,2,5,2]), 3)), [1,2,2,4,3,5])
            self.assertEqual(self.convb(sol(self.convf([1,4,3,0,5,2]), 2)), [1,0,4,3,5,2])

if __name__ == "__main__":
    unittest.main()
