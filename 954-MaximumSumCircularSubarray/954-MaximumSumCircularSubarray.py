# Last updated: 5/29/2026, 11:54:04 AM
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total=sum(nums)
        max_far=max_ans=nums[0]
        min_far=min_ans=nums[0]
        for i in range(1,len(nums)):
            max_far=max(nums[i],max_far+nums[i])
            max_ans=max(max_ans,max_far)
            min_far=min(nums[i],min_far+nums[i])
            min_ans=min(min_ans,min_far)
        if max_ans<0:
            return max_ans
        return max(max_ans,total-min_ans)