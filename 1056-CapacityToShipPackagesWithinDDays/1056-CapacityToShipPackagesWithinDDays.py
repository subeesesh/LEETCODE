# Last updated: 5/29/2026, 11:53:43 AM
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def help(maxsum):
            curr=0
            parts=1
            for n in weights:
                if curr+n>maxsum:
                    parts+=1
                    curr=n
                else:
                    curr+=n
            return parts<=days
        l=max(weights)
        r=sum(weights)
        while l<r:
            mid=(l+r)//2
            if help(mid):
                r=mid
            else:
                l=mid+1
        return l