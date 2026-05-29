# Last updated: 5/29/2026, 11:51:53 AM
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        row=len(grid)
        col=len(grid[0])
        lps=[[1]*col for _ in range(row)]
        lp=1
        rp=1
        for i in range(row):
            for j in range(col):
                lps[i][j]=(lp*lps[i][j])%12345
                lp=(lp*grid[i][j])%12345
        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                lps[i][j]=(rp*lps[i][j])%12345
                rp=(rp*grid[i][j])%12345
        return lps