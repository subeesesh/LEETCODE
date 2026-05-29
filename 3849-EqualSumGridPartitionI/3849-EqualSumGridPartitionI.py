# Last updated: 5/29/2026, 11:51:37 AM
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        row=len(grid)
        col=len(grid[0])
        total_sum=0
        total_sum+=sum(sum(grid[i]) for i in range(row))
        hor_sum=0
        for r in range(row):
            hor_sum+=sum(grid[r])
            if total_sum-hor_sum==hor_sum:
                return True
        ver_sum=[sum(x) for x in zip(*grid)]
        ps=0
        for c in ver_sum:
            ps+=c
            if total_sum-ps==ps:
                return True
        return False