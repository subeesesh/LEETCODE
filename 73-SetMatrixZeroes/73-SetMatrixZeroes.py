# Last updated: 5/29/2026, 11:59:40 AM
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])
        first_row = False
        first_col = False
        for j in range(col):
            if matrix[0][j] == 0:
                first_row = True
        for i in range(row):
            if matrix[i][0] == 0:
                first_col = True
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_row:
            for j in range(col):
                matrix[0][j] = 0
        if first_col:
            for i in range(row):
                matrix[i][0] = 0