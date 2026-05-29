# Last updated: 5/29/2026, 11:53:18 AM
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        wsum=0
        for i in range(k):
            wsum+=cardPoints[i]
        max_val=wsum
        for i in range(k):
            wsum=wsum-cardPoints[k-i-1]+cardPoints[len(cardPoints)-i-1]
            max_val=max(max_val,wsum)
        return max_val