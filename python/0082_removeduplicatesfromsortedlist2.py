import unittest
from typing import Optional, List
from helpers import *
from collections import Counter

class _ (Helpers):
    '''
    82: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
    Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only 
    distinct numbers from the original list. Return the linked list sorted as well.
 
    '''
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        q1 = ListNode(-1, head)
        q_h = q1
        q2 = head        
        while q2 and q2.next:
            dup = 0
            while q2 and q2.val==q1.next.val:
                q2 = q2.next
                dup += 1
            if dup > 1:
                q1.next = q2 # skip all of duplicates, but we don't progress in q1
            else:
                q1 = q1.next
                q1.next = q2
        return q_h.next 

class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.deleteDuplicates]:
            self.assertEqual(self.convb(sol(self.convf([1,1,1,2,3]))), [2,3])
            self.assertEqual(self.convb(sol(self.convf([1,1]))), [])

if __name__ == "__main__":
    unittest.main()
