import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    124: https://leetcode.com/problems/binary-tree-maximum-path-sum/
    A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
    A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
    The path sum of a path is the sum of the node's values in the path.
    Given the root of a binary tree, return the maximum path sum of any non-empty path.
    '''        
    def sol1(self, root: Optional[TreeNode]) -> int:
        max_path = float("-inf") # placeholder to be updated
        def get_max_gain(node):
            nonlocal max_path # This tells that max_path is not a local variable
            if not node: return 0 				
            gain_on_left = max(get_max_gain(node.left), 0) # Read the part important observations
            gain_on_right = max(get_max_gain(node.right), 0) # Read the part important observations
            current_max_path = node.val + gain_on_left + gain_on_right # Read first three images of going down the recursion stack
            max_path = max(max_path, current_max_path) # Read first three images of going down the recursion stack
            return node.val + max(gain_on_left, gain_on_right) # Read the last image of going down the recursion stack
        get_max_gain(root) # Starts the recursion chain
        return max_path

    def sol2(self, root: Optional[TreeNode]) -> int:
        '''
        This doesnt pass LT
        '''
        if not root: return 0
        if not root.left and not root.right: return root.val
        def helper(node):
            if not node: return 0, 0 # max loop, max depth
            if not node.left and not node.right: return node.val, 0
            left_val, total_left = helper(node.left)
            right_val, total_right = helper(node.right)
            if total_left == 0 and total_right == 0: # the nodes one both sides are single or nones
                total_center = left_val + right_val + node.val
            else:
                total_center = max(total_left, total_right) # we propagate the max up
            if left_val == 0: total_path = right_val
            elif right_val == 0: total_path = left_val
            else: total_path = max(left_val, right_val)
            total_path = max(total_path, total_path + node.val, node.val)
            if total_path == node.val: total_center = 0
            return total_path, total_center
        a,b = helper(root)
        if b == 0: return a
        return max(a,b)


class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1, self.sol2]:
            self.assertEqual(sol(self.tree_convf([1,2,3])), 6)
            tree = self.tree_convf([-10,9,20,None,None,15,7])
            tree.print_tree_stack()
            self.assertEqual(sol(tree), 42)
                             
if __name__ == "__main__":
    unittest.main()
