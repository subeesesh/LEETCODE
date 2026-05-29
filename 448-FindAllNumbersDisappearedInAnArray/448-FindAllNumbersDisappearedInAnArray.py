# Last updated: 5/29/2026, 11:55:32 AM
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i=0
        while i<len(nums):
            ind=nums[i]-1
            if nums[i]!=nums[ind]:
                nums[i],nums[ind]=nums[ind],nums[i]
            else:
                i+=1
        res=[]
        for i in range(len(nums)):
            if nums[i]!=i+1:
                res.append(i+1)
        return res
