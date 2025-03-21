import unittest
from typing import Optional, List
from helpers import *

class _ (ListNode):
    '''
    24: https://leetcode.com/problems/swap-nodes-in-pairs/description/
    Given a linked list, swap every two adjacent nodes and return its head. 
    You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
    '''
    def sol1(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        q = ListNode(val = -1, next = head)  
        q_h = q
        while q.next and q.next.next: # we check that the next two nodes can be modified
            tail = q.next.next
            q.next.next = q.next.next.next
            tail.next = q.next
            q.next = tail
            q = q.next.next            
        return q_h.next
 
class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        self.assertEqual(self.convb(self.sol1(self.convf([1,2,3,4]))), [2,1,4, 3])
        self.assertEqual(self.convb(self.sol1(self.convf([1]))), [1])
        self.assertEqual(self.convb(self.sol1(self.convf([]))), [])

if __name__ == "__main__":
    unittest.main()