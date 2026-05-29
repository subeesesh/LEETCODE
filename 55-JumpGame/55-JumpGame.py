# Last updated: 5/29/2026, 12:00:08 PM
class Solution:
    def canJump(self, nums):
        maxReach = 0
        for i in range(len(nums)):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + nums[i])
        return True
