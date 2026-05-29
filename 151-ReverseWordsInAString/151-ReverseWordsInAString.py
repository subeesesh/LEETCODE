# Last updated: 5/29/2026, 11:58:01 AM
class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        rl=l[::-1]
        o=""
        for i in rl:
            o+=i+" "
        return o.strip()