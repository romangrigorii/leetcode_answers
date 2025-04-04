import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    174: https://leetcode.com/problems/dungeon-game/description/

    The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.

    The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

    Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).

    To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

    Return the knight's minimum initial health so that he can rescue the princess.

    Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

    '''
    def sol1(self, dungeon: List[List[int]]) -> int:
        R = len(dungeon)
        C = len(dungeon[0])
        dungeon = [q + [float('inf')] for q in dungeon] + [[float('inf') for a in range(C+1)]]
        dungeon[R-1][C] = 1
        dungeon[R][C-1] = 1
        for r in range(R-1,-1,-1):
            for c in range(C-1,-1,-1):
                dungeon[r][c] = max(1,min(dungeon[r][c+1], dungeon[r+1][c]) - dungeon[r][c])
        return dungeon[0][0]
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol([[-2,-3,3],[-5,-10,1],[10,30,-5]]), 7)
            self.assertEqual(sol([[0]]), 1)

if __name__ == "__main__":
    unittest.main()
