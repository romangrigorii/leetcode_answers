import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    92: https://leetcode.com/problems/reverse-linked-list-ii/
    Given the head of a singly linked list and two integers left and right where left <= right, 
    reverse the nodes of the list from position left to position right, and return the reversed list. 
    '''
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        q = ListNode(1,head)
        q_h = q
        left -=1
        while left and q:
            q = q.next
            left -= 1
            right -=1
        if left>0: return q_h.next
        cur = q.next
        tmp = None
        tmpptr = None
        while right:
            next = cur.next
            cur.next = tmp
            tmp = cur
            if not tmpptr: tmpptr = tmp
            cur = next
            right -= 1
        q.next = tmp
        tmpptr.next = next
        return q_h.next


class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.reverseBetween]:
            self.assertEqual(self.convb(sol(self.convf([1,2,3,4,5]), 2, 4)), [1,4,3,2,5])

if __name__ == "__main__":
    unittest.main()
    