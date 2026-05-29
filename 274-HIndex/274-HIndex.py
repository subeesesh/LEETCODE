# Last updated: 5/29/2026, 11:56:31 AM
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        for i in range(len(citations)):
            if citations[i]>=len(citations)-i:
                return len(citations)-i
        return 0