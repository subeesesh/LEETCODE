# Last updated: 5/29/2026, 11:53:47 AM
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1:
            return 1
        indeg=[0]*(n+1)
        outdeg=[0]*(n+1)
        for i in range(len(trust)):
            outdeg[trust[i][0]]+=1
            indeg[trust[i][1]]+=1
        for i in range(n+1):
            if indeg[i]==n-1 and outdeg[i]==0:
                return i
        return -1