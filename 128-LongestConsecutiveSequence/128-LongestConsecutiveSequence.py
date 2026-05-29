# Last updated: 5/29/2026, 11:58:32 AM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=set(nums)
        max_len=0
        for n in num:
            if (n-1) not in num:
                leng=0
                while(n+leng) in num:
                    leng+=1
                max_len=max(max_len,leng)
        return max_len