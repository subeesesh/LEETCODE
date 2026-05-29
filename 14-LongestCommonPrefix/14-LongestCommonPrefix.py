# Last updated: 5/29/2026, 12:01:10 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        f=strs[0]
        l=strs[-1]
        i=0
        while i<len(f) and f[i]==l[i]:
            i+=1
        return f[:i]