import unittest
from typing import Optional, List
from helpers import *

class _ (Helpers):
    '''
    22: https://leetcode.com/problems/generate-parentheses/
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    '''
    def sol1(self, n: int) -> List[str]:
        '''
        This is a stack solution
        '''
        # the solution utilied the fact that for some n pairs of parentheses, there must be n left and n right parenthesis
        res = []
        s = [("(", 1, 0)]
        while s:
            x, l, r = s.pop()
            if l < r or l > n or r > n: # l cannot be less than r because that means we have a parenthesis we cannot close, also we can't exceed l == n and r == n
                continue
            if l == n and r == n: # when we close the loop
                res.append(x)
            s.append((x+"(", l+1, r))
            s.append((x+")", l, r+1))
        return res
    
    def sol2(self, n: int) -> List[str]:
        def backtrack(parenthesis, opened, closed):
            '''
            This is a dfs solution
            '''
            # save solution
            if len(parenthesis) == 2*n:
                res.append(parenthesis)
            # add opened parenthesis
            if opened < n:
                backtrack(parenthesis + "(", opened+1, closed)
            # add closed parenthesis
            if closed < opened:
                backtrack(parenthesis + ")", opened, closed+1)
        res = []
        backtrack("", 0, 0)
        return res

    def sol3(self, n: int) -> List[int]:
        '''
        This is dfs solution
        '''
        out = []
        def helper(sofar, l , r):
            if l == n and r == n: out.append(sofar)
            else:
                if l<n: helper(sofar + '(', l+1, r)
                if r<l: helper(sofar + ')', l, r+1)
        helper('', 0, 0)
        return out
           

class test(unittest.TestCase, _ , Helpers):
    def test_(self):       
        for sol in [self.sol1, self.sol2, self.sol3]:
            self.assertTrue(self.equal_lists(sol(n = 1),  ["()"]))
            self.assertTrue(self.equal_lists(sol(n = 2 ),  ["()()", "(())"]))
            self.assertTrue(self.equal_lists(sol(n = 3), ['()()()', '()(())', '(())()', '(()())', '((()))']))

if __name__ == "__main__":
    unittest.main()