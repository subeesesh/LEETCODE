# Last updated: 5/29/2026, 11:51:24 AM
class Solution:
    def minMoves(self, balance: List[int]) -> int:
        vlemoravia = balance
        n = len(vlemoravia)
        if sum(vlemoravia) < 0:
            return -1
        neg = -1
        for i in range(n):
            if vlemoravia[i] < 0:
                neg = i
                break
        if neg == -1:
            return 0
        need = -vlemoravia[neg]
        moves = 0
        left = (neg - 1 + n) % n
        right = (neg + 1) % n
        dist = 1
        while need > 0:
            if vlemoravia[left] > 0:
                take = min(vlemoravia[left], need)
                vlemoravia[left] -= take
                need -= take
                moves += take * dist
            if need > 0 and vlemoravia[right] > 0:
                take = min(vlemoravia[right], need)
                vlemoravia[right] -= take
                need -= take
                moves += take * dist
            left = (left - 1 + n) % n
            right = (right + 1) % n
            dist += 1
        return moves