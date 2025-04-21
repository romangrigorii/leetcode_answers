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
        st = 0
        lists.sort(key = lambda x: x.val if x else -1) # sort by first value to start
        while not lists[st]: st += 1 # skip the None elemenets at the start
        if st == len(lists): return None
        out = ListNode()
        qh = out
        
        def place(lists, st, en):
            start = st
            st += 1
            if comp.val<lists[st.val]: return lists
            mid = st
            while st<en:
                mid = (st+en)//2
                if comp.val < lists[mid].val: st = mid + 1
                else: en = mid - 1
            return lists[:st] + lists[st+1:mid] + [comp] + lists[mid:]
        
        while st < len(lists)-1:
            new = ListNode(lists[st].val, None)
            out.next = new
            out = out.next
            lists[st] = lists[st].next
            if lists[st]:
                lists = place(lists, st, len(lists)-1)
            else:
                st+=1

        return qh.next

 
class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        for sol in [self.sol1, self.sol2]:
            self.assertEqual(self.convb(sol([self.convf([1,4,5]),self.convf([1,3,4]),self.convf([2,6])])), [1,1,2,3,4,4,5,6])

if __name__ == "__main__":
    unittest.main()