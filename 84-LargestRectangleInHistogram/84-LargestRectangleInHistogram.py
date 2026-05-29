# Last updated: 5/29/2026, 11:59:27 AM
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        stack=[]
        max_ele=0
        for i in range(n):
            while stack and heights[i]<heights[stack[-1]]:
                h=heights[stack.pop()]
                if not stack:
                    width=i
                else:
                    width=i-stack[-1]-1
                max_ele=max(max_ele,h*width)
            stack.append(i)
        while stack:
            h=heights[stack.pop()]
            if not stack:
                width=n
            else:
                width=n-stack[-1]-1
            max_ele=max(max_ele,h*width)
        return max_ele