# Last updated: 5/29/2026, 11:53:09 AM
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + (1 if low % 2 == 1 or high % 2 == 1 else 0)