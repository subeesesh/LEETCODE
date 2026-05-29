# Last updated: 5/29/2026, 11:57:58 AM
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        max_far=nums[0]
        min_far=nums[0]
        result=nums[0]
        for i in range(1,len(nums)):
            current=nums[i]
            temp_far=max(current,max_far*current,min_far*current)
            min_far=min(current,max_far*current,min_far*current)
            max_far=temp_far
            result=max(result,max_far)
        return result