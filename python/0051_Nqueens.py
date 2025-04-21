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
        self.lists = [] 
        self.search(n, 0, intercepts, [])
        return self.lists

    def search(self,n,ystart,intercepts, potential):
        interceptsnew = set()
        for x in range(n):
            if (x,ystart) not in intercepts:
                potentialnew = ['.'*x + 'Q' + '.'*(n-x-1)]
                if ystart == n-1:
                    self.lists += [potential + potentialnew] # if this is the last one we are adding just add it 
                else:
                    interceptsnew = [(x,i) for i in range(ystart+1, n)] + [(i+x-ystart,i) for i in range(ystart+1, n) if (i+x-ystart)<n] + [(x-i+ystart,i) for i in range(ystart+1, n) if (x-i+ystart)>=0]
                    self.search(n, ystart+1, intercepts | set(interceptsnew), potential + potentialnew)
    
    def sol2(self, n: int) -> List[List[str]]:
        out = []
        def bfs(y, not_allowed, cur):
            if y == n: out.append(cur)
            else:
                for i in range(n): # sweep the horizontal axis of the board
                    if (i,y) not in not_allowed:                        
                        cur_str = '.' * i + 'Q' + (n-i-1)*'.'
                        not_allowed_new = set()
                        for j in range(1, n):
                            if y + j < n:
                                not_allowed_new.add((i, y+j))
                                if i + j < n: not_allowed_new.add((i+j, y+j))
                                if i - j >=0: not_allowed_new.add((i-j, y+j))
                        bfs(y+1, not_allowed | not_allowed_new, cur + [cur_str])
        bfs(0, set(), [])
        return out

class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        for sol in [self.sol1, self.sol2]:
            self.equal_lists(sol(4), [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]])

if __name__ == "__main__":
    unittest.main()
