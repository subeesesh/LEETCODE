# Last updated: 5/29/2026, 11:52:38 AM
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        diff=[0]*2051
        for b,d in logs:
            diff[b]+=1
            diff[d]-=1
        curr=0
        max_y=0
        ans=0
        for i in range(len(diff)):
            curr+=diff[i]
            if curr>max_y:
                max_y=curr
                ans=i
                
        return ans