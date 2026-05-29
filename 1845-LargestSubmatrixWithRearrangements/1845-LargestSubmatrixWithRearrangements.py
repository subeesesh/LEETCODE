# Last updated: 5/29/2026, 11:52:50 AM
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        row=len(matrix)
        col=len(matrix[0])
        ps = [[0 for _ in range(col)] for _ in range(row)]
        for j in range(col):
            sum=0
            for i in range(row):
                sum+=int(matrix[i][j])
                if matrix[i][j]==0:
                    sum=0
                ps[i][j]=sum
        max_ans=0
        for i in range(row):
            j=sorted(ps[i],reverse=True)
            for k in range(col):
                area=j[k]*(k+1) 
                max_ans=max(max_ans,area)
        return max_ans
