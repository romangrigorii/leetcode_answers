import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    206: https://leetcode.com/problems/reverse-linked-list
    Given the head of a singly linked list, reverse the list, and return the reversed list.
    '''
    def sol1(self, head: ListNode):
        head2 = None
        while head:
            head2 = ListNode(head.val, head2)
            head = head.next
        return head2

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(self.convb(sol(self.convf([1,2,3,4,5]))), [5,4,3,2,1])

if __name__ == "__main__":
    unittest.main()
