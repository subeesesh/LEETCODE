# Last updated: 5/29/2026, 11:55:52 AM
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s1=iter(t)
        return all(char in s1 for char in s)