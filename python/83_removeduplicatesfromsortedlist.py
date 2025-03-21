import unittest
from typing import Optional, List
from helpers import *
from collections import Counter

class _ :
    '''
    83: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
    Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
    Return the linked list sorted as well.
 
    '''
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        q1 = head
        q2 = head    
        while q2:
            while q2 and q2.val==q1.val:
                q2 = q2.next
            q1.next = q2
            q1 = q1.next
        return head
        


class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.deleteDuplicates]:
            self.assertEqual(self.convb(sol(self.convf([1,1,1,2,3]))), [1,2,3])
            self.assertEqual(self.convb(sol(self.convf([1,1]))), [1])

if __name__ == "__main__":
    unittest.main()
