import unittest
from typing import Optional, List
from helpers import *

class _ (Helpers):
    '''
    19: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
    Given the head of a linked list, remove the nth node from the end of the list and return its head.
    '''
    def sol1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        Pass through the array forming a stack and then pop values from the stack until we reach kth, which we delete
        '''     
        if not head: 
            return None        
        if not head.next and n == 1:
            return None
        if n == 0: 
            return head
        q = ListNode(val = -1, next = head)
        self.helper(q, n)
        return q.next

    def helper(self, q, target):
        if not q.next:
            return 0, q
        else:
            a, b = self.helper(q.next, target)
            if a+1 == target:
                q.next = b.next
                return -1, q
            else:
                if a == -1:
                    return -1, q
                return a+1, q
    
    def sol2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        Go through the array twice
        '''
        if not head: return head
        k = 0
        q = ListNode(-1,head)
        q_h = q
        while head:
            k+=1
            head = head.next
        # k represents the length of the list
        k -= n
        while k>0:
            q = q.next
            k-=1
        if q.next: q.next = q.next.next
        return q_h.next
    
    def sol3(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        We create two pointers, one is ahead the other by n. Once the faster one reaches the end, we remove whatever node the slower is on.
        '''
        q1 = ListNode(-1, head)
        q2 = ListNode(-1, head)
        q_h = q1
        while n>0:
            q2 = q2.next
            n -=1
        while q2.next:
            q1 = q1.next
            q2 = q2.next
        if q1.next: q1.next = q1.next.next 
        return q_h.next
 
class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        for sol in [self.sol1, self.sol2,  self.sol3]:
            self.assertEqual(self.convb(sol(self.convf([1]), 1)), [])
            self.assertEqual(self.convb(sol(self.convf([1]), 0)), [1])
            self.assertEqual(self.convb(sol(self.convf([1,2,3,4,5]), 1)), [1,2,3,4])
            self.assertEqual(self.convb(sol(self.convf([1,2,3,4,5]), 2)), [1,2,3,5])

if __name__ == "__main__":
    unittest.main()