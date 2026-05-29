# Last updated: 5/29/2026, 11:51:38 AM
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        def can(k):
            diff = [0] * (n + 1)
            for i in range(k):
                l, r, val = queries[i]
                diff[l] += val
                if r + 1 < n:
                    diff[r + 1] -= val

            curr = 0
            for i in range(n):
                curr += diff[i]
                if curr < nums[i]:   # not enough decrements
                    return False
            return True

        left, right = 0, len(queries)
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
