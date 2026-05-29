# Last updated: 5/29/2026, 11:51:26 AM
class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        sums=sum(nums[:k])
        suml=sum(nums[-k:])
        return abs(sums-suml)