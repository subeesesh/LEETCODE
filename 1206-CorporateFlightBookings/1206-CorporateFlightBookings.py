# Last updated: 5/29/2026, 11:53:33 AM
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff=[0]*n
        for i in bookings:
            start=i[0]
            end=i[1]
            val=i[2]
            diff[start-1]+=val
            if end<n:
                diff[end]-=val
        ps=[]
        ps.append(diff[0])
        for i in range(1,len(diff)):
            ps.append(ps[i-1]+diff[i])
        return ps
