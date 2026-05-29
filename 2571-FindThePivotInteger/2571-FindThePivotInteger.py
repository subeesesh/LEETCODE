# Last updated: 5/29/2026, 11:52:01 AM
class Solution:
    def pivotInteger(self, n: int) -> int:
        t=n*(n+1)//2
        l=0
        for i in range(1,n+1):
            t-=i
            if l==t:
                return i
            l+=i
        return -1