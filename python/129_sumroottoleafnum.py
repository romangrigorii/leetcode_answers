import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    129: https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
    You are given the root of a binary tree containing digits from 0 to 9 only.

    Each root-to-leaf path in the tree represents a number.

    For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
    Return the total sum of all root-to-leaf numbers. Test cases are generated so that the 
    answer will fit in a 32-bit integer.

    A leaf node is a node with no children.
    '''
    def sol1(self, root) -> int:
        all_nums = []
        def append_str(root, str_so_far):
            if root: 
                str_so_far_ = str_so_far + str(root.val)
                if root.left: 
                    append_str(root.left, str_so_far_)
                if root.right: 
                    append_str(root.right, str_so_far_)
                if not root.left and not root.right: 
                    all_nums.append(str_so_far_)
        append_str(root,'0')
        return sum([int(q) for q in all_nums])

class test(unittest.TestCase, _, Helpers):
    def test_(self):  
        tree1 = self.tree_convf([1,2,3])
        #tree1.print_tree_stack()  
        tree2 = self.tree_convf([4,9,0,5,1])
        #tree2.print_tree_stack()
        for sol in [self.sol1]:
            self.assertEqual(sol(tree1), 25)
            self.assertEqual(sol(tree2), 1026)

if __name__ == "__main__":
    unittest.main()
