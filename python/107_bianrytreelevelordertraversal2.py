import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    107: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
    Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. 
    (i.e., from left to right, level by level from leaf to root).
    '''
    def sol1(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = {}
        def helper(depth, node):            
            if node and node.val!=None:
                helper(depth+1, node.left)
                helper(depth+1, node.right)
                out.setdefault(depth, []).append(node.val)
        helper(0, root)
        if not out: return []
        return [out[i] for i in range(max(out.keys()),-1,-1)]
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol(root = self.tree_convf([3,9,20,None, None,15,7])),[[15,7],[9,20],[3]])
            


if __name__ == "__main__":
    unittest.main()
