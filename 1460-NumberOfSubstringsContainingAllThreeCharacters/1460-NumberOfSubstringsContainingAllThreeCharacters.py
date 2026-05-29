# Last updated: 5/29/2026, 11:53:21 AM
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {'a': 0, 'b': 0, 'c': 0}
        l = 0
        res = 0
        n = len(s)
        for r in range(n):
            count[s[r]] += 1
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                res += n - r
                count[s[l]] -= 1
                l += 1
        return res
