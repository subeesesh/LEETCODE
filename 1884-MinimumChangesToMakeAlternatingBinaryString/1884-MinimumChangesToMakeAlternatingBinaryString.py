# Last updated: 5/29/2026, 11:52:48 AM
class Solution:
    def minOperations(self, s: str) -> int:
        c, j, n = 0, 0, len(s)
        for ch in s:
            if int(ch) == j:
                c += 1
            j ^= 1
        return min(c, n - c)