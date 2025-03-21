import unittest
from typing import Optional, List
from helpers import *

class _ (Helpers):
    '''
    23: https://leetcode.com/problems/merge-k-sorted-lists/
    You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
    Merge all the linked-lists into one sorted linked-list and return it.
    '''
    def sol1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:   
        lst = []
        out = ListNode()
        q = out
        for ln in lists:
            while ln:
                lst.append(ln.val)
                ln = ln.next
        lst.sort()
        for e in lst:
            new = ListNode(e,None)
            q.next = new
            q = q.next
        return out.next

 
class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        self.assertEqual(self.convb(self.sol1([self.convf([1,4,5]),self.convf([1,3,4]),self.convf([2,6])])), [1,1,2,3,4,4,5,6])

if __name__ == "__main__":
    unittest.main()