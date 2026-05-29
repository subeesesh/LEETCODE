# Last updated: 5/29/2026, 11:55:26 AM
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        peri=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    peri+=4
                    if j+1<col and grid[i][j+1]==1 :
                        peri-=2
                    if i+1<row and grid[i+1][j]==1 :
                        peri-=2  
        return peri