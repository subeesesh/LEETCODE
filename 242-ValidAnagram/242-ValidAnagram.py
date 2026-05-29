# Last updated: 5/29/2026, 11:56:42 AM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        result={}
        for i in range(len(s)):
            result[s[i]]=result.get(s[i],0)+1
            result[t[i]]=result.get(t[i],0)-1
        for count in result.values():
            if count!=0:
                return False
        return True