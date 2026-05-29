# Last updated: 5/29/2026, 11:57:06 AM
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row=len(matrix)
        col=len(matrix[0])
        c={}
        def help(i,j):
            if i>=row or j>=col:
                return 0
            if (i,j) not in c:
                down=help(i+1,j)
                right=help(i,j+1)
                diag=help(i+1,j+1)
                c[(i,j)]=0
                if matrix[i][j]=='1':
                    c[(i,j)]=1+min(down,right,diag)
            return c[(i,j)]
        help(0,0)
        return max(c.values())**2