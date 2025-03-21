import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    103: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
    Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
    (i.e., from left to right, then right to left for the next level and alternate between).
    '''
    def sol1(self, root):
        if not root: return []
        queue = deque([root])
        result, direction = [], 1
        
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:  queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(level[::direction])
            direction *= (-1)
        return result
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.sol1]:
            self.assertEqual(sol(self.tree_convf([3,9,20,7,8,15,7])), [[3],[20,9],[7,8,15,7]])

if __name__ == "__main__":
    unittest.main()
