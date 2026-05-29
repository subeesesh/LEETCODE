# Last updated: 5/29/2026, 11:54:37 AM
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        t=sum(nums)
        l=0
        for i in range(len(nums)):
            t-=nums[i]
            if l==t:
                return i
            l+=nums[i]
        return -1