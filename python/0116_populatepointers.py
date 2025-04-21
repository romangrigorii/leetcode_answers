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
    116: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
    You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. 
    The binary tree has the following definition:

    struct Node {
        int val;
        Node *left;
        Node *right;
        Node *next;
    }
    Populate each next pointer to point to its next right node. 
    If there is no next right node, the next pointer should be set to NULL.

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
