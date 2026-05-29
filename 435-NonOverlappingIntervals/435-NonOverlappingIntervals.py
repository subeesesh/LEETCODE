# Last updated: 5/29/2026, 11:55:38 AM
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        p=intervals[0][1]
        res=0
        for s,e in intervals[1:]:
            if s>=p:
                p=e
            else:
                res+=1
                p=min(e,p)
        return res