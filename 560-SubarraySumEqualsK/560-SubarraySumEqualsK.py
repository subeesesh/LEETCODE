# Last updated: 5/29/2026, 11:54:59 AM
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq={0:1}
        ps,count=0,0
        for i in range(len(nums)):
            ps+=nums[i]
            if ps-k in freq:
                count+=freq[ps-k]
            freq[ps]=freq.get(ps,0)+1
        return count