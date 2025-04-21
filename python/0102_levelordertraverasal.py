import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    102: https://leetcode.com/problems/binary-tree-level-order-traversal/description/
    Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
    '''
    def sol1(self, root):
        ol = []
        def helper(pos, rt):
            if rt: 
                while pos>len(ol):
                    ol.extend([None]*(len(ol)+1))
                ol[pos-1] = rt.val
                helper(pos*2, rt.left)
                helper(pos*2+1, rt.right)
        helper(1, root)
        i, out = 0, []
        i = 0
        while 2**i < len(ol):
            out.append([q for q in ol[2**i - 1: 2**(i+1) - 1] if q])
            i+=1
        return out
    
    def sol2(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []
        if not root: return out
        self.traverse(out, root, 0)
        return out

    def traverse(self, out, root, level):
        if root:
            if len(out) > level:
                out[level].append(root.val)
            else:
                out.append([root.val])            
            self.traverse(out, root.left, level+1)
            self.traverse(out, root.right, level+1)

class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.sol1, self.sol2]:
            self.assertEqual(sol(self.tree_convf([3,9,20,None,None,15,7])), [[3],[9,20],[15,7]])

if __name__ == "__main__":
    unittest.main()
