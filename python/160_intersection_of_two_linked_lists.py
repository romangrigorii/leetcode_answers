import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    160: https://leetcode.com/problems/intersection-of-two-linked-lists/
    Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
    If the two linked lists have no intersection at all, return null.

    For example, the following two linked lists begin to intersect at node c1:


    The test cases are generated such that there are no cycles anywhere in the entire linked structure.

    Note that the linked lists must retain their original structure after the function returns.

    Custom Judge:

    The inputs to the judge are given as follows (your program is not given these inputs):

    intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
    listA - The first linked list.
    listB - The second linked list.
    skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
    skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
    The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. 
    If you correctly return the intersected node, then your solution will be accepted.

    '''
    def sol1(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A, B = headA, headB
        while A!=B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(self.convb(sol(self.convf([4,1,8,4,5]), self.convf([5,6,1,8,4,5]))), [8,4,5])

if __name__ == "__main__":
    unittest.main()
