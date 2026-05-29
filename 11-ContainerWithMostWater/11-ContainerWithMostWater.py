# Last updated: 5/29/2026, 12:01:13 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxw=0
        i=0
        j=len(height)-1
        while(i<j):
            maxw=max(maxw,min(height[i],height[j])*(j-i))
            if(height[i]<height[j]):
                i+=1
            else:
                j-=1
        return maxw