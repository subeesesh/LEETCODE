# Last updated: 5/29/2026, 11:54:46 AM
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        maxans=0
        def dfs(i,j):
            if i>=row or j>=col or i<0 or j<0 or grid[i][j]==0:
                return 0
            grid[i][j]=0
            count=1
            count+=dfs(i+1,j)
            count+=dfs(i-1,j)
            count+=dfs(i,j+1)
            count+=dfs(i,j-1)
            return count
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    maxans=max(maxans,dfs(i,j))
        return maxans
