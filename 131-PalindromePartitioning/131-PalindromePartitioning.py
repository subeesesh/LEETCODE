# Last updated: 5/29/2026, 11:58:27 AM
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispa(sub):
            return sub==sub[::-1]
        def back(start,path):
            if start==len(s):
                res.append(path.copy())
                return 
            for i in range(start,len(s)):
                sub=s[start:i+1]
                if ispa(sub):
                    path.append(sub)
                    back(i+1,path)
                    path.pop()
        res=[]
        back(0,[])
        return res