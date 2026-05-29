# Last updated: 5/29/2026, 12:00:01 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=s.split()
        return len(l[len(l)-1])