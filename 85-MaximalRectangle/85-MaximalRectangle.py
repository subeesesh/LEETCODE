# Last updated: 5/29/2026, 11:59:22 AM
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        row=len(matrix)
        col=len(matrix[0])
        ps = [[0 for _ in range(col)] for _ in range(row)]
        for j in range(col):
            sum=0
            for i in range(row):
                sum+=int(matrix[i][j])
                if matrix[i][j]=='0':
                    sum=0
                ps[i][j]=sum
        def his(arr):
            stack=[]
            max_ele=0
            for i in range(len(arr)):
                while stack and arr[i]<arr[stack[-1]]:
                    h=arr[stack.pop()]
                    if not stack:
                        width=i
                    else:
                        width=i-stack[-1]-1
                    max_ele=max(max_ele,h*width)
                stack.append(i)
            n=len(arr)
            while stack:
                h=arr[stack.pop()]
                if not stack:
                    width=n
                else:
                    width=n-stack[-1]-1
                max_ele=max(max_ele,h*width)
            return max_ele
        max_ans=0
        for i in ps:
            max_ans=max(max_ans,his(i))
        return max_ans

                