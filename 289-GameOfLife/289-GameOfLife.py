# Last updated: 5/29/2026, 11:56:24 AM
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                live = 0
                if i > 0 and j > 0 and board[i - 1][j - 1] % 2 == 1:
                    live += 1
                if i > 0 and board[i - 1][j] % 2 == 1:
                    live += 1
                if i > 0 and j < col - 1 and board[i - 1][j + 1] % 2 == 1:
                    live += 1
                if j > 0 and board[i][j - 1] % 2 == 1:
                    live += 1
                if j < col - 1 and board[i][j + 1] % 2 == 1:
                    live += 1
                if i < row - 1 and j > 0 and board[i + 1][j - 1] % 2 == 1:
                    live += 1
                if i < row - 1 and board[i + 1][j] % 2 == 1:
                    live += 1
                if i < row - 1 and j < col - 1 and board[i + 1][j + 1] % 2 == 1:
                    live += 1
                if board[i][j] % 2 == 1:
                    if live == 2 or live == 3:
                        board[i][j] += 2
                else:
                    if live == 3:
                        board[i][j] += 2
        for i in range(row):
            for j in range(col):
                board[i][j] //= 2
