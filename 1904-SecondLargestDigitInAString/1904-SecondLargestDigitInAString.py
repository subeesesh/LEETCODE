# Last updated: 5/29/2026, 11:52:45 AM
class Solution:
    def secondHighest(self, s: str) -> int:
        sett=set(s)
        strr=[]
        for i in sett:
            if i.isnumeric():
                strr.append(int(i))
        strr.sort()
        return strr[len(strr)-2] if len(strr)>0 and strr[0]-strr[len(strr)-1]!=0 else -1
