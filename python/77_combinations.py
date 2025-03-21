import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    77: https://leetcode.com/problems/combinations/description/
    Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
    You may return the answer in any order.
    '''
    def combine(self, n: int, k: int) -> List[List[int]]:
        out = [[]]
        for _ in range(k):
            if out[0] == []:
                out = [[i] for i in range(1, n+1)]             
            else:
                out = [[i] + c for c in out for i in range(1, c[0])]
        return out

    def combine2(self, n: int, k: int) -> List[List[int]]:
        out = []
        def combine2_h(st, sofar, left):
            if left == 0: out.append(sofar)
            else:
                if st<n:
                    combine2_h(st+1, sofar + [st], left-1)
                    combine2_h(st+1, sofar, left)

        combine2_h(1, [], k)
        return out


class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.combine, self.combine2]:
            self.equal_lists(sol(4,2),[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]])

if __name__ == "__main__":
    unittest.main()
