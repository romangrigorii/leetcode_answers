import unittest
from typing import Optional, List
from helpers import *

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class _(Helpers) :    
    '''
    125: https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
    Given a binary tree

    struct Node {
        int val;
        Node *left;
        Node *right;
        Node *next;
    }
    Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

    Initially, all next pointers are set to NULL.
    '''
    def sol1(self, s: str, t: str) -> int:
        pass

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:            
            # self.assertEqual(sol(), -1)
            pass



if __name__ == "__main__":
    unittest.main()
