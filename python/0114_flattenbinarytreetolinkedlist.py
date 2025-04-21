import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    114: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
    Given the root of a binary tree, flatten the tree into a "linked list": 
    The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
    The "linked list" should be in the same order as a pre-order traversal of the binary tree.
    '''
    def sol1(self, root: Optional[TreeNode]) -> None:
        if not root: return root
        stack = [root]
        qh = TreeNode()
        qh_h = qh
        while stack:
            q = stack.pop()
            if q:
                stack.append(q.right)
                stack.append(q.left)
                qh.right = TreeNode(q.val)
                qh = qh.right
        return qh_h.right

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            s = self.tree_convf([1,2,5,3,4,None,6])
            s.print_tree_stack()
            s2 = sol(s)
            s2.print_tree_stack()
            self.assertEqual(self.tree_convb(sol(s)), [1,None,2,None,3,None,4,None,5,None,6])


if __name__ == "__main__":
    unittest.main()
