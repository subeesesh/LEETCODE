# Last updated: 5/29/2026, 11:54:30 AM
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j={}
        jj=0
        for i in jewels:
            j[jj]=i
            jj+=1
        count=0
        for i in stones:
            if i in j.values():
                count+=1

        return count