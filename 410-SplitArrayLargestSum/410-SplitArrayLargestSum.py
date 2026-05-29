# Last updated: 5/29/2026, 11:55:44 AM
class Solution:
    def splitArray(self, nums, k):
        def canSplit(maxSum):
            curr = 0
            parts = 1
            for n in nums:
                if curr + n > maxSum:
                    parts += 1
                    curr = n
                else:
                    curr += n
            return parts <= k

        l, r = max(nums), sum(nums)
        while l < r:
            mid = (l + r) // 2
            if canSplit(mid):
                r = mid
            else:
                l = mid + 1
        return l
