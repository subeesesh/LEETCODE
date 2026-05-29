# Last updated: 5/29/2026, 11:53:35 AM
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff=[0]*1001
        for i in trips:
            start=i[1]
            end=i[2]
            val=i[0]
            diff[start]+=val
            diff[end]-=val
        curr=0
        for i in range(len(diff)):
            curr+=diff[i]
            if curr>capacity:
                return False
        return True

