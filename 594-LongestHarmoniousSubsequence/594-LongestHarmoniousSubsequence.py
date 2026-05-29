# Last updated: 5/29/2026, 11:54:56 AM
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        si,max=0,0
        l=0
        for li in range(1,len(nums)):
            if(nums[li]-nums[si]==1):
                l=li-si+1
                if(l>max):
                    max=l
            while(nums[li]-nums[si]>1 and si<li):
                si+=1
        return max