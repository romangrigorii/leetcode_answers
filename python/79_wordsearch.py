import unittest
from typing import Optional, List
from helpers import *
from collections import Counter

class _ :
    '''
    79: https://leetcode.com/problems/word-search/submissions/1248705287/
    Given an m x n grid of characters board and a string word, return true if word exists in the grid.
    The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally
    or vertically neighboring. The same letter cell may not be used more than once.
    '''
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        lw = len(word)

        co_board = Counter(sum(board,[]))
        co_word = Counter(word)
        for c in co_word:
            if (co_word[c] - co_board[c]) > 0: return False
        
        seen = set()
        def dfs(r,c, l):
            if l == lw: return True            
            if r<0 or c<0 or r>=R or c>=C or word[l]!=board[r][c] or (r,c) in seen: return False
            seen.add((r,c))
            res = dfs(r+1,c,l+1) or dfs(r,c+1,l+1) or dfs(r-1,c,l+1) or dfs(r,c-1,l+1)
            seen.remove((r,c))
            return res

        for r in range(R):
            for c in range(C):
                if dfs(r,c,0): return True
        
        return False

class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.exist]:
            self.assertEqual(sol([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"), True)

if __name__ == "__main__":
    unittest.main()
