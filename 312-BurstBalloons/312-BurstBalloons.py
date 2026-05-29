# Last updated: 5/29/2026, 11:56:13 AM
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums=[1]+nums+[1]
        n=len(nums)
        dp=[[0 for _ in range(n)] for _ in range(n)]
        for i in range(2,n):
            for j in range(n-i):
                k=i+j
                for x in range(j+1,k):
                    dp[j][k]=max(dp[j][k],dp[j][x]+dp[x][k]+nums[k]*nums[j]*nums[x])
        return dp[0][n-1]