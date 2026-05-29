# Last updated: 5/29/2026, 12:00:18 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp=defaultdict(list)
        for s in strs:
            key=''.join(sorted(s))
            mp[key].append(s)
        return list(mp.values())