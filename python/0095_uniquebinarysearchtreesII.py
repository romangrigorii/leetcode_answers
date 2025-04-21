import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    95: https://leetcode.com/problems/unique-binary-search-trees-ii/
    Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n 
    nodes of unique values from 1 to n. Return the answer in any order.
    '''
    def sol1(self, n: int) -> List[Optional[TreeNode]]:
        def trees(first, last):
            return [TreeNode(mid, left, right) for mid in range(first, last+1) for left in trees(first, mid-1) for right in trees(mid+1, last)] or [None]
        return trees(1, n)   
    
        
    def sol2(self, n: int) -> List[Optional[TreeNode]]:
        def trees(start, end):
            nodes = []
            for m in range(start, end):
                nodes_left = trees(start, m)
                nodes_right = trees(m+1, end)
                if not nodes_left: nodes_left = [None]
                if not nodes_right: nodes_right = [None]
                for l in nodes_left:
                    for r in nodes_right:
                        nodes.append(TreeNode(m, l, r))
            return nodes
        return trees(1,n+1)   

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1, self.sol2]:
            self.equal_lists(list(map(self.tree_convb, sol(3))), [[1,None,2,None,3],[1,None,3,2],[2,1,3],[3,1,None,None,2],[3,2,None,1]])
            


if __name__ == "__main__":   
    unittest.main()
