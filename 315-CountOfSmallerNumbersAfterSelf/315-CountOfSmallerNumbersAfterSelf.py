# Last updated: 5/29/2026, 11:56:09 AM
from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        res = [0] * len(nums)
        arr = list(enumerate(nums))   # (index, value)

        def merge_sort(left, right):
            if left == right:
                return [arr[left]]

            mid = (left + right) // 2
            left_part = merge_sort(left, mid)
            right_part = merge_sort(mid + 1, right)

            return merge(left_part, right_part)

        def merge(left, right):
            merged = []
            i = j = 0
            count = 0

            while i < len(left) and j < len(right):

                if left[i][1] <= right[j][1]:
                    res[left[i][0]] += count
                    merged.append(left[i])
                    i += 1
                else:
                    count += 1
                    merged.append(right[j])
                    j += 1

            while i < len(left):
                res[left[i][0]] += count
                merged.append(left[i])
                i += 1

            while j < len(right):
                merged.append(right[j])
                j += 1

            return merged

        merge_sort(0, len(nums) - 1)

        return res