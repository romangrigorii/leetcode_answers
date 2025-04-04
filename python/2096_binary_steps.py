import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    2096: https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/description/
    '''
    def sol1(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        d = deque([("", root)])
        sol = ['','']
        def helper(vals):
            while len(sol[0])==0 or len(sol[1])==0:
                d_new = d.pop()
                if d_new[1]:
                    if d_new[1].val == vals[0]: sol[0] = 'x' + d_new[0]
                    if d_new[1].val == vals[1]: sol[1] = 'x' + d_new[0]
                    d.appendleft((d_new[0] + "L", d_new[1].left))
                    d.appendleft((d_new[0] + "R", d_new[1].right))
        helper([startValue, destValue])
        idx = 0
        while idx < len(sol[0]) and idx < len(sol[1]) and sol[0][idx]==sol[1][idx]:
            idx+=1
        return 'U'*len(sol[0][idx:]) + sol[1][idx:]

    def sol2(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find(node: TreeNode, target: int) -> Optional[List[str]]:
            if node.val == target:
                return []
            if node.left:
                path = find(node.left, target)
                if path is not None:
                    path.append('L')
                    return path
            if node.right:
                path = find(node.right, target)
                if path is not None:
                    path.append('R')
                    return path
            return None
        
        path1 = find(root, startValue)
        path2 = find(root, destValue)

        while len(path1) and len(path2) and path1[-1] == path2[-1]:
            path1.pop()
            path2.pop()

        return 'U' * len(path1) + ''.join(reversed(path2))

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1, self.sol2]:
            self.assertEqual(sol(self.tree_convf([5,1,2,3,None,6,4]),3,6), 'UURL')

if __name__ == "__main__":
    unittest.main()
