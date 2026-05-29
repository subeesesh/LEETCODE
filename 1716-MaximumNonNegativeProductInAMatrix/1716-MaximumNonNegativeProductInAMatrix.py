# Last updated: 5/29/2026, 11:53:01 AM
class Solution:
    MOD=10**9+7
    def maxProductPath(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        max_dp=[[0 for _ in range(col)] for _ in range(row)]
        min_dp=[[0 for _ in range(col)] for _ in range(row)]
        max_dp[0][0]=min_dp[0][0]=grid[0][0]
        for i in range(1,row):
            max_dp[i][0]=min_dp[i][0]=grid[i][0]*max_dp[i-1][0]
        for j in range(1,col):
            max_dp[0][j]=min_dp[0][j]=grid[0][j]*max_dp[0][j-1]
        for i in range(1,row):
            for j in range(1,col):
                max_dp[i][j]=max(max_dp[i-1][j]*grid[i][j],min_dp[i-1][j]*grid[i][j],max_dp[i][j-1]*grid[i][j],min_dp[i][j-1]*grid[i][j])
                min_dp[i][j]=min(max_dp[i-1][j]*grid[i][j],min_dp[i-1][j]*grid[i][j],max_dp[i][j-1]*grid[i][j],min_dp[i][j-1]*grid[i][j])
        res=max_dp[row-1][col-1]
        return res % self.MOD if res>=0 else -1