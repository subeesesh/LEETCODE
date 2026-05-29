# Last updated: 5/29/2026, 11:53:04 AM
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total=sum(nums)
        rem=total%p
        if rem==0:
            return 0
        ps=0
        freq={0:-1}
        min_len=len(nums)
        for right in range(len(nums)):
            ps=(ps+nums[right])%p
            need=(ps-rem)%p
            if need in freq:
                min_len=min(min_len,right-freq[need])
            freq[ps]=right
        return min_len if min_len<len(nums) else -1