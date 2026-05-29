# Last updated: 5/29/2026, 12:01:27 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        map=set()
        max_len=float('-inf')
        left=0
        for right in range(len(s)):
            while s[right] in map:
                map.remove(s[left])
                left+=1
            map.add(s[right])
            max_len=max(max_len,right-left+1)
        return max_len