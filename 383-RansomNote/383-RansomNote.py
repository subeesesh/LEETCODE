# Last updated: 5/29/2026, 11:55:55 AM
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map=collections.Counter(magazine)
        for c in ransomNote:
            if c not in map or map[c]==0:
                return False
            map[c]-=1
        return True
