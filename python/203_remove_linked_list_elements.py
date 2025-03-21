import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    203: https://leetcode.com/problems/remove-linked-list-elements/
    Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, 
    and return the new head.
    '''
    def sol1(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        q = ListNode(next = head)
        q_h = q
        while q and q.next:
            if q.next.val == val: 
                q.next = q.next.next
            else: q = q.next
        return q_h.next

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(self.convb(sol(self.convf([1,2,6,3,4,5,6]), 6)),[1,2,3,4,5])
            self.assertEqual(self.convb(sol(self.convf([]), 6)),[])
            self.assertEqual(self.convb(sol(self.convf([7,7,7,7]), 7)),[])


if __name__ == "__main__":
    unittest.main()
