# Last updated: 5/29/2026, 11:59:36 AM
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        map=defaultdict(int)
        map1=Counter(t)
        want=len(map1)
        have=0
        res=""
        len_res=float("inf")
        l=0
        for r in range(len(s)):
            c=s[r]
            map[c]+=1
            if c in map1 and map1[c]==map[c]:
                have+=1
            while have==want:
                if (r-l+1)<len_res:
                    res=s[l:r+1]
                    len_res=r-l+1
                map[s[l]]-=1
                if s[l] in map1 and map[s[l]]<map1[s[l]]:
                    have-=1
                l+=1
        return res


        