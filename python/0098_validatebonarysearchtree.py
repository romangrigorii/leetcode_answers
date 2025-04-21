import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    98: https://leetcode.com/problems/validate-binary-search-tree/
    Given the root of a binary tree, determine if it is a valid binary search tree (BST).
    A valid BST is defined as follows:
    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
    '''

    def sol1(self, root):
        def self1_helper(root, lessThan = float('inf'), largerThan = float('-inf')):
            if not root or not root.val:
                return True
            if root.val <= largerThan or root.val >= lessThan:
                return False
            return self1_helper(root.left, min(lessThan, root.val), largerThan) and \
                self1_helper(root.right, lessThan, max(root.val, largerThan))
        return self1_helper(root)

class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.sol1]:
            self.assertEqual(sol(self.tree_convf([5,1,4,None,None,3,6])), False)
            #print(self.tree_convb(self.tree_convf([5,4,6,None,None,3,7])))
            self.assertEqual(sol(self.tree_convf([5,4,6,None,None,3,7])), False)

if __name__ == "__main__":
    unittest.main()
