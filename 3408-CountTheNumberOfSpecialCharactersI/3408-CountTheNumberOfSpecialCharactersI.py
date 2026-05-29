# Last updated: 5/29/2026, 11:51:44 AM
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        map=set()
        res=set()
        count=0
        wordl=sorted(word,reverse="True")
        for i in wordl:
            if 'A'<=i<='Z':
                if i.lower() in map:
                    res.add(i)
            map.add(i)
        return len(res)