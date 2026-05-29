# Last updated: 5/29/2026, 11:51:43 AM
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "X":
                    grid[i][j] = 1
                if grid[i][j] == "Y":
                    grid[i][j] = -1
                if grid[i][j] == ".":
                    grid[i][j] = 0
        ps = [[0] * m for _ in range(n)]
        xps = [[0] * m for _ in range(n)]
        count = 0
        for i in range(n):
            for j in range(m):
                ps[i][j] = grid[i][j]
                xps[i][j] = 1 if grid[i][j] == 1 else 0
                if i > 0:
                    ps[i][j] += ps[i - 1][j]
                    xps[i][j] += xps[i - 1][j]
                if j > 0:
                    ps[i][j] += ps[i][j - 1]
                    xps[i][j] += xps[i][j - 1]
                if i > 0 and j > 0:
                    ps[i][j] -= ps[i - 1][j - 1]
                    xps[i][j] -= xps[i - 1][j - 1]
                if ps[i][j] == 0 and xps[i][j] > 0:
                    count += 1
        return count