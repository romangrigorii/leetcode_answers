import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    139: https://leetcode.com/problems/word-break
    Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
    '''
    def sol1(self, head: Optional[ListNode]) -> bool:
        q = []
        qh = head
        qh2 = head
        while head:
            q.append(head.val)
            head = head.next
        q.sort()
        i = 0
        while qh:
            qh.val = q[i]
            qh = qh.next
            i+=1
        return qh2

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(self.convb(sol(self.convf([4,2,1,3]))), [1,2,3,4])
            self.assertEqual(self.convb(sol(self.convf([-1,5,3,4,0]))), [-1,0,3,4,5])
            self.assertEqual(self.convb(sol(self.convf([]))), [])

if __name__ == "__main__":
    unittest.main()
