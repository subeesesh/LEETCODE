# Last updated: 5/29/2026, 11:57:50 AM
class Solution(object):
    def maximumGap(self, nums):
        nums.sort()
        if len(nums)<2:
            return 0
        diff=0
        max_diff=0
        for i in range(1,len(nums)):
            diff=nums[i]-nums[i-1]
            max_diff=max(max_diff,diff)
        return max_diff
        