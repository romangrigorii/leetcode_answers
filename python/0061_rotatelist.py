import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    61: https://leetcode.com/problems/rotate-list/
    Given the head of a linked list, rotate the list to the right by k places.
    '''
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        
        '''
        if not head or not head.next or k == 0: return head
        q = head
        q2 = head
        list_len = 0
        while k:
            list_len+=1
            q = q.next
            k-=1
            if not q.next:
                k %= list_len
                q = q2
        while q.next:
            q2 = q2.next # this pointer starts at the head
            q = q.next # this pointer starts k entries into the list
        q.next = head # we set the rest of the list to head
        q3 = q2 # q2 is now located at the start of the resulting list
        q2 = q2.next 
        q3.next = None # we break the loop
        return q2
            

class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.rotateRight]:
            self.assertEqual(self.convb(sol(self.convf([1,2,3,4,5]), 2)), [4,5,1,2,3])

if __name__ == "__main__":
    unittest.main()
    