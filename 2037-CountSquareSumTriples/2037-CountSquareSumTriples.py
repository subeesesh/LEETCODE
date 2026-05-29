# Last updated: 5/29/2026, 11:52:32 AM
class Solution:
    def countTriples(self, n: int) -> int:
        count=0
        for i in range(1,n+1):
            for j in range(1,n+1):
                k=i**2+j**2
                s=int(k**0.5)
                if s*s==k and s<=n:
                    count+=1
        return count