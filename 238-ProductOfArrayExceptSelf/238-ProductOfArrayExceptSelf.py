# Last updated: 5/29/2026, 11:56:50 AM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        out=[1]*n
        lps=1
        rps=1
        for i in range(n):
            out[i]*=lps
            lps*=nums[i]
        for i in range(n-1,-1,-1):
            out[i]*=rps
            rps*=nums[i]
        return out