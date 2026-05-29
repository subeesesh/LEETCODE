# Last updated: 5/29/2026, 11:56:36 AM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(nums[len(nums)-1]):
            if i!=nums[i]:
                return i
        return nums[-1]+1