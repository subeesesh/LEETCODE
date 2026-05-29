# Last updated: 5/29/2026, 11:55:29 AM
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        res=[points[0]]
        for i,j in points[1:]:
            end=res[-1][1]
            if i<=end:
                res[-1][1]=min(j,end)
            else:
                res.append([i,j])
        return len(res)