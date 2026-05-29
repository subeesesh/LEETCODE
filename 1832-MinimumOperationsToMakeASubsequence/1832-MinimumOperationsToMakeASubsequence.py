# Last updated: 5/29/2026, 11:52:51 AM
class Solution:
    def minOperations(self, target, arr):
        n, nums = len(target), []
        D = {target[i]: i for i in range(n)}
        res = [D[i] for i in arr if i in D.keys()]
        for i in res:
            j = bisect.bisect_left(nums, i)
            if j == len(nums): nums.append(i)
            else: nums[j] = i
        return n - len(nums)