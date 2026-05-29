# Last updated: 5/29/2026, 11:58:39 AM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_far=0
        curr_max=0
        for i in range(1,len(prices)):
            diff=prices[i]-prices[i-1]
            curr_max=max(diff,curr_max+diff)
            max_far=max(max_far,curr_max)
        return max_far