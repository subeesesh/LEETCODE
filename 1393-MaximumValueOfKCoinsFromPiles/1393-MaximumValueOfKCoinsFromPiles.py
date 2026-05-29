# Last updated: 5/29/2026, 11:53:29 AM
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n=len(piles)
        dp=[[-1] *(k+1) for _ in range(n)]
        def dfs(i,coins):
            if i==n:
                return 0
            if dp[i][coins]!=-1:
                return dp[i][coins]
            
            dp[i][coins]=dfs(i+1,coins)
            currpile=0
            for j in range(min(coins,len(piles[i]))):
                currpile+=piles[i][j]
                dp[i][coins]=max(dp[i][coins],currpile+dfs(i+1,coins-j-1))
            return dp[i][coins]
        return dfs(0,k)