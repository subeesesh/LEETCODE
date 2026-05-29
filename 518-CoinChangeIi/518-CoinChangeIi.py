# Last updated: 5/29/2026, 11:55:14 AM
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0]*(amount+1)
        dp[0]=1
        for c in coins:
            for i in range(c,(amount+1)):
                dp[i]=dp[i-c]+dp[i]
        return dp[-1]