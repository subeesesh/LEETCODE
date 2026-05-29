# Last updated: 5/29/2026, 11:54:35 AM
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = {}

        def dfs(r1, c1, r2):
            c2 = r1 + c1 - r2

            # invalid
            if r1 >= n or c1 >= n or r2 >= n or c2 >= n:
                return -10**9
            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return -10**9

            # reached end
            if r1 == n-1 and c1 == n-1:
                return grid[r1][c1]

            if (r1, c1, r2) in dp:
                return dp[(r1, c1, r2)]

            # cherries collected
            cherries = grid[r1][c1]
            if r1 != r2:
                cherries += grid[r2][c2]

            best = max(
                dfs(r1+1, c1, r2+1),   # both down
                dfs(r1, c1+1, r2),     # A right, B down
                dfs(r1+1, c1, r2),     # A down, B right
                dfs(r1, c1+1, r2+1)    # both right
            )

            dp[(r1, c1, r2)] = cherries + best
            return dp[(r1, c1, r2)]

        return max(0, dfs(0, 0, 0))
            
