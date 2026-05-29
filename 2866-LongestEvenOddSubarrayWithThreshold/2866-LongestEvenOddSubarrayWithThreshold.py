# Last updated: 5/29/2026, 11:51:55 AM
class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans = 0
        curr_len = 0

        for i in range(len(nums)):
            if nums[i] > threshold:
                curr_len = 0
                continue
            if (
                i == 0 or
                nums[i - 1] > threshold or
                nums[i] % 2 == nums[i - 1] % 2
            ):
                if nums[i] % 2 == 0:
                    curr_len = 1
                else:
                    curr_len = 0
            else:
                curr_len += 1
            ans = max(ans, curr_len)

        return ans
