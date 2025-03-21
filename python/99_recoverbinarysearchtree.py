import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    99: https://leetcode.com/problems/recover-binary-search-tree/
    GYou are given the root of a binary search tree (BST), where the values of exactly two nodes 
    of the tree were swapped by mistake. Recover the tree without changing its structure.
    '''
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        dlist = [None, None, None]
        def inorder(node, dlist):
            if not node or not node.val:
                return
            inorder(node.left, dlist)
            if (dlist[0] and node.val<dlist[0].val):
                if not dlist[1]: dlist[1] = dlist[0]
                dlist[2] = node
            dlist[0] = node
            inorder(node.right, dlist)
        
        inorder(root, dlist)
        dlist[1].val, dlist[2].val = dlist[2].val, dlist[1].val
        return root

class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.recoverTree]:
            self.assertEqual(self.tree_convb(sol(self.tree_convf([1,3,None,None,2]))), [3,1,None,None,2])


if __name__ == "__main__":
    unittest.main()
