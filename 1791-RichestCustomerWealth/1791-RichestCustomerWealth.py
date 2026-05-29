# Last updated: 5/29/2026, 11:52:56 AM
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_far=0
        sum_ele=0
        for i in accounts:
            sum_ele=sum(i)
            max_far=max(max_far,sum_ele)
        return max_far