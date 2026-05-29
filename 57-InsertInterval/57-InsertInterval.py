# Last updated: 5/29/2026, 12:00:02 PM
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def merge(intervals):
            intervals.sort(key=lambda x: x[0])
            res=[intervals[0]]
            for i,j in intervals[1:]:
                end=res[-1][1]
                if i<=end:
                    res[-1][1]=max(j,end)
                else:
                    res.append([i,j])
            return res
        intervals.append(newInterval)
        return merge(intervals)