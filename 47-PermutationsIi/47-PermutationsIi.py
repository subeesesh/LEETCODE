# Last updated: 5/29/2026, 12:00:21 PM
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def next_perm(perm: List[int]) -> List[int]:
            # 1) Find the first index i from the right such that perm[i] < perm[i + 1]
            i = n - 2
            while i >= 0 and perm[i] >= perm[i + 1]:
                i -= 1

            # If no pivot is found, we are at the last permutation
            if i < 0:
                return perm[::-1]

            # 2) Find the smallest element greater than perm[i]
            j = i + 1
            while j + 1 < n and perm[j + 1] > perm[i]:
                j += 1

            # 3) Swap pivot and successor
            perm[i], perm[j] = perm[j], perm[i]

            # 4) Reverse the suffix starting at pivot + 1
            perm[i + 1:] = perm[:i:-1]
            return perm

        permutations = [nums]
        current = nums

        while True:
            current = next_perm(current.copy())
            if current == permutations[0]:
                break
            permutations.append(current)

        return permutations