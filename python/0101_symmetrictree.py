import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    101: https://leetcode.com/problems/symmetric-tree/description/
    Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
    '''
    def isSymmetric(self, root):
        if not root:
            return True        
        q = deque([root.left, root.right])        
        while q:
            t1, t2 = q.popleft(), q.popleft()
            if not t1 and not t2:
                continue
            elif (not t1 or not t2) or (t1.val != t2.val):
                return False            
            q += [t1.left, t2.right, t1.right, t2.left]
            
        return True

class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.isSymmetric]:
            self.assertEqual(sol(self.tree_convf([1,2,2,3,4,4,3])), True)

if __name__ == "__main__":
    unittest.main()
