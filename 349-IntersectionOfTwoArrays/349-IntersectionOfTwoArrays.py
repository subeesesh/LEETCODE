# Last updated: 5/29/2026, 11:56:01 AM
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        def binary_search(search_arr: list[int], target: int) -> bool:
            start, end = 0, len(search_arr) - 1

            while start <= end:
                middle = (start + end) // 2

                if search_arr[middle] < target:
                    start = middle + 1
                elif search_arr[middle] > target:
                    end = middle - 1
                else:
                    return True

            return False

        # force nums1 to be the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # sort the larger array
        nums2.sort()

        res = set()
        for n in nums1:
            if binary_search(nums2, n):
                res.add(n)

        return list(res)