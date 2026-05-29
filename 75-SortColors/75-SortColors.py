# Last updated: 5/29/2026, 11:59:37 AM
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l,m,h=0,0,len(nums)-1
        while(m<=h):
            if nums[m]==0:
                nums[l],nums[m]=nums[m],nums[l]
                m+=1
                l+=1
            elif nums[m]==1:
                m+=1
            else:
                nums[h],nums[m]=nums[m],nums[h]
                h-=1
        return nums
        