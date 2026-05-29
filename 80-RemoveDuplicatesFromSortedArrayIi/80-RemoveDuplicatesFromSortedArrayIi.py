# Last updated: 5/29/2026, 11:59:28 AM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr=1
        count=0
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                count=0
                nums[curr]=nums[i]
                curr+=1
            else:
                count+=1
                if count<=1:
                    nums[curr]=nums[i]
                    curr+=1
        return curr