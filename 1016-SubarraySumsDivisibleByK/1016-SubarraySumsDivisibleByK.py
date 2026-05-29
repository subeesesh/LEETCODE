# Last updated: 5/29/2026, 11:53:52 AM
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ps=0
        count=0
        freq={0:1}
        for i in range(len(nums)):
            ps=(ps+nums[i])%k
            if ps in freq:
                count+=freq[ps]
            freq[ps]=freq.get(ps,0)+1
        return count