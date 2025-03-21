import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    37: https://leetcode.com/problems/sudoku-solver/description/
    Write a program to solve a Sudoku puzzle by filling the empty cells.
    A sudoku solution must satisfy all of the following rules:
    Each of the digits 1-9 must occur exactly once in each row.
    of the digits 1-9 must occur exactly once in each column.
    Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
    The '.' character indicates empty cells.
    '''
    def solveSudoku(self, board: List[List[str]]) -> None:
        def candidate_nums(row, col):
            return rows[row] & cols[col] & boxes[box_index(row, col)]

        def nexts(row, col):
            if col < 8:
                col += 1
            elif row < 8:
                row += 1
                col = 0
            else:
                row = -1
                col = -1
            return row, col

        solved = False

        def backtrack(row, col):
            nonlocal solved
            if row == -1 and col == -1:
                solved = True
                return
            if board[row][col] == '.':
                cand_nums = candidate_nums(row, col)
                for num in cand_nums:
                    set_num(num, row, col)
                    next_row, next_col = nexts(row, col)
                    backtrack(next_row, next_col)
                    if solved:
                        return
                    revert_num(num, row, col)
            else:
                next_row, next_col = nexts(row, col)
                backtrack(next_row, next_col)

        def set_num(num, row, col):
            board[row][col] = num
            rows[row].discard(num)
            cols[col].discard(num)
            boxes[box_index(row, col)].discard(num)

        def revert_num(num, row, col):
            board[row][col] = '.'
            rows[row].add(num)
            cols[col].add(num)
            boxes[box_index(row, col)].add(num)

        def box_index(row, col):
            return (row // 3) * 3 + (col // 3)

        nums = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        rows = {}
        cols = {}
        boxes = {}
        for i in range(9):
            rows[i] = set(nums)
            cols[i] = set(nums)
            boxes[i] = set(nums)
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    rows[r].discard(board[r][c])
                    cols[c].discard(board[r][c])
                    boxes[box_index(r, c)].discard(board[r][c])

        backtrack(0, 0)
        return board
    
board1_unsolved = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
board1_solved = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]

class test(unittest.TestCase, _ , Helpers):
    def test_(self):
        self.assertEqual(self.solveSudoku(board1_unsolved), board1_solved)

if __name__ == "__main__":
    unittest.main()
