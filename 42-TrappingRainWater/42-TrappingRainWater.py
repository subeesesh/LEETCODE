# Last updated: 5/29/2026, 12:00:29 PM
class Solution:
    def trap(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        lm=0
        rm=0
        water=0
        while i<j:
            if height[i]<height[j]:
                if height[i]>lm:
                    lm=height[i]
                else:
                    water+=lm-height[i]
                i+=1
            else:
                if height[j]>rm:
                    rm=height[j]
                else:
                    water+=rm-height[j]
                j-=1
        return water
