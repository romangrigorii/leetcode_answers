import unittest
from typing import Optional, List
from helpers import *

class _ (ListNode):
    '''
    25: https://leetcode.com/problems/reverse-nodes-in-k-group/description/
    Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
    k is a positive integer and is less than or equal to the length of the linked list. 
    If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
    You may not alter the values in the list's nodes, only nodes themselves may be changed.
    '''
    def sol1(self, head: Optional[ListNode], k) -> Optional[ListNode]: 
        q = ListNode(val = -1, next = head)
        p = head
        tail = head # we point to the first element in p which will be last element in rev
        rev = None
        kk = k
        while kk and p:
            p = p.next
            kk -= 1 
        if kk:
            return tail # if we reachd the end of list but didn't get to k == 0 we just return the tail
        else:
            kk = k
            p = head
            while kk and p:
                temp = p.next
                p.next = rev
                rev = p
                p = temp
                kk-=1
            q.next = rev
            tail.next = self.sol1(p,k)
        return q.next

 
class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        self.assertEqual(self.convb(self.sol1(self.convf([1,2,3,4,5]), 2)),[2,1,4,3,5])
        self.assertEqual(self.convb(self.sol1(self.convf([1,2,3,4,5]), 3)),[3,2,1,4,5])

if __name__ == "__main__":
    unittest.main()