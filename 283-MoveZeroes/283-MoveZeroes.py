# Last updated: 5/29/2026, 11:56:28 AM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s=-1
        f=0
        while(f<len(nums)):
            if(nums[f]!=0):
                nums[s+1]=nums[f]
                s+=1
                f+=1
            else:
                f+=1
        while(s<len(nums)-1):
            nums[s+1]=0
            s+=1
        