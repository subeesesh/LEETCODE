# Last updated: 5/29/2026, 11:55:23 AM
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if total < abs(target) or (total + target) % 2 == 1:
            return 0

        subset = (target + total) // 2
        n = len(nums)

        dp = [[0] * (subset + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(subset + 1):

                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][subset]