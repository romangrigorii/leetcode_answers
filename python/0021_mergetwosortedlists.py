import unittest
from typing import Optional, List
from helpers import *

class _ (Helpers):
    '''
    19: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
    Given the head of a linked list, remove the nth node from the end of the list and return its head.
    '''
    def sol1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:     
        q = ListNode()
        q_h = q
        while list1 and list2:
            if list1.val < list2.val:
                q.next = list1
                list1 = list1.next                
            else:
                q.next = list2
                list2 = list2.next
            q = q.next
        if list1: q.next = list1
        if list2: q.next = list2
        return q_h.next

 
class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        self.assertEqual(self.convb(self.sol1(self.convf([1,2,4]), self.convf([1,3,4]))),[1,1,2,3,4,4])

if __name__ == "__main__":
    unittest.main()