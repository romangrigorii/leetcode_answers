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

    def sol2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeList(l1, l2):
            dummy = ListNode()
            head = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    head.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    head.next = ListNode(l2.val)
                    l2 = l2.next
                head = head.next
            if l1:
                head.next = l1
            if l2:
                head.next = l2
            return dummy.next
        
        while len(lists) > 1:
            length = len(lists)
            temp = []
            for l in range(0, length, 2):
                l1 = lists[l]
                l2 = lists[l+1] if l+1 < length else None
                temp.append(mergeList(l1, l2))
            lists = temp
        return lists[0] if lists else None

 
class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        for sol in [self.sol1, self.sol2]:
            self.assertEqual(self.convb(sol([self.convf([1,4,5]),self.convf([1,3,4]),self.convf([2,6])])), [1,1,2,3,4,4,5,6])

if __name__ == "__main__":
    unittest.main()