# Last updated: 5/29/2026, 11:57:47 AM
import statistics
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return statistics.mode(nums)