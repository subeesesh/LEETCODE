# Last updated: 5/29/2026, 12:00:32 PM
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
                while 1<=nums[i]<=len(nums) and nums[nums[i]-1]!=nums[i]:
                    temp=nums[nums[i]-1]
                    nums[nums[i]-1]=nums[i]
                    nums[i]=temp
        for i in range(len(nums)):
            if i+1!=nums[i]:
                return i+1
        return len(nums)+1