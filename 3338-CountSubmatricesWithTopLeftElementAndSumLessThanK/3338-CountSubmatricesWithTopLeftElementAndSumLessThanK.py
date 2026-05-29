# Last updated: 5/29/2026, 11:51:47 AM
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        row = len(grid)
        col = len(grid[0])
        ps = [[0] * col for _ in range(row)]
        count = 0
        for i in range(row):
            for j in range(col):
                ps[i][j] = grid[i][j]
                if i > 0:
                    ps[i][j] += ps[i-1][j]
                if j > 0:
                    ps[i][j] += ps[i][j-1]
                if i > 0 and j > 0:
                    ps[i][j] -= ps[i-1][j-1]
                if ps[i][j] <= k:
                    count += 1
        return count
             