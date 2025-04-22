import unittest
from typing import Optional, List
from helpers import *
from collections import Counter
class _ :
    '''
    51: https://leetcode.com/problems/n-queens/
    The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
    Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
    Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
    '''
    def sol1(self, n: int) -> List[List[str]]:
        intercepts = set()
        self.tot = 0 
        self.search(n, 0, intercepts)
        return self.tot

    def search(self,n,ystart,intercepts):
        interceptsnew = set()
        for x in range(n):
            if (x,ystart) not in intercepts:
                if ystart == n-1:
                    self.tot+=1
                else:
                    interceptsnew = [(x,i) for i in range(ystart+1, n)] + [(i+x-ystart,i) for i in range(ystart+1, n) if (i+x-ystart)<n] + [(x-i+ystart,i) for i in range(ystart+1, n) if (x-i+ystart)>=0]
                    self.search(n, ystart+1, intercepts | set(interceptsnew))

class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        for sol in [self.sol1]:
            self.assertEqual(sol(4), 2)
            self.assertEqual(sol(1), 1)

if __name__ == "__main__":
    unittest.main()
