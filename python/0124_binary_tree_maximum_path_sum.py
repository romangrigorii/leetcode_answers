import unittest
from typing import Optional
from helpers import *
from helpers import TreeNode

class _(Helpers):
    '''
    124: https://leetcode.com/problems/binary-tree-maximum-path-sum/
    Given the root of a binary tree, return the maximum path sum of any non-empty path.
    '''
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        Optimal solution using postorder DFS. At each node, compute the maximum gain from left and right,
        and update the global max path sum if the path through this node is higher.
        '''
        max_path = float('-inf')
        def get_max_gain(node):
            nonlocal max_path
            if not node:
                return 0
            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)
            # Path sum including both children and current node
            current_path = node.val + left_gain + right_gain
            max_path = max(max_path, current_path)
            # Return max gain if continuing the same path upwards
            return node.val + max(left_gain, right_gain)
        get_max_gain(root)
        return max_path

class test(unittest.TestCase, _, Helpers):
    def test_basic(self):
        for sol in [self.maxPathSum]:
            self.assertEqual(sol(self.tree_convf([1,2,3])), 6)
            self.assertEqual(sol(self.tree_convf([-10,9,20,None,None,15,7])), 42)
            self.assertEqual(sol(self.tree_convf([2,-1])), 2)
            self.assertEqual(sol(self.tree_convf([-3])), -3)

    def test_all_negative(self):
        for sol in [self.maxPathSum]:
            self.assertEqual(sol(self.tree_convf([-2,-1,-3])), -1)
            self.assertEqual(sol(self.tree_convf([-5,-4,-6,-7,-8])), -4)

    def test_single_node(self):
        for sol in [self.maxPathSum]:
            self.assertEqual(sol(self.tree_convf([7])), 7)
            self.assertEqual(sol(self.tree_convf([-7])), -7)

    def test_debug(self):
        """Debug test to understand the algorithm behavior"""
        tree = self.tree_convf([1,None,2,None,3,None,4])
        result = self.maxPathSum(tree)
        print(f"Debug: For tree [1,None,2,None,3,None,4], result = {result}")
        # Let's also check what the tree structure looks like
        print("Tree structure:")
        tree.print_tree_stack()

    def test_skewed(self):
        for sol in [self.maxPathSum]:
            # For right-skewed tree [1,None,2,None,3,None,4], max path is 7 (1+2+4)
            self.assertEqual(sol(self.tree_convf([1,None,2,None,3,None,4])), 7)
            # For left-skewed tree [1,2,None,3,None,4,None], max path is 6 (1+2+3)
            self.assertEqual(sol(self.tree_convf([1,2,None,3,None,4,None])), 6)

    def test_large(self):
        for sol in [self.maxPathSum]:
            # Large balanced tree
            vals = [i for i in range(1, 32)]  # 31 nodes
            tree = self.tree_convf(vals)
            # The max path is the sum of the rightmost path (as built by tree_convf)
            self.assertEqual(sol(tree), 102)

if __name__ == "__main__":
    unittest.main()
