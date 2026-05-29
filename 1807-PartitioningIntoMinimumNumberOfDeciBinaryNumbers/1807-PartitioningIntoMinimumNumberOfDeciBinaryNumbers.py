# Last updated: 5/29/2026, 11:52:52 AM
class Solution:
    def minPartitions(self, n: str) -> int:
        l=[]
        for i in n:
            l.append(int(i))
        return max(l)