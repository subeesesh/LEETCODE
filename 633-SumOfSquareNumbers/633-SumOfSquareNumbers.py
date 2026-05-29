# Last updated: 5/29/2026, 11:54:53 AM
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start=0
        end=int(c**0.5)
        while start<=end:
            summ=start**2+end**2
            if summ==c:
                return True
            elif summ>c:
                end-=1
            else:
                start+=1
        return False