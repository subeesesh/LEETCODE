# Last updated: 5/29/2026, 11:51:39 AM
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n=len(nums)
        diff=[0]*n
        for l,r in queries:
            diff[l]+=1
            if r+1<n:
                diff[r+1]-=1
        curr=0
        for i in range(n):
            curr+=diff[i]
            if(curr<nums[i]):
                return False
        return True

