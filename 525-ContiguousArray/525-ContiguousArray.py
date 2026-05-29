# Last updated: 5/29/2026, 11:55:09 AM
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ps=0
        freq={0:-1}
        max_len=0
        for i in range(len(nums)):
            if nums[i]==1:
                ps+=1
            else :
                ps-=1
            if ps in freq:
                max_len=max(max_len,i-freq[ps])
            else:
                freq[ps]=i
        return max_len

