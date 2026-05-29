# Last updated: 5/29/2026, 12:01:24 PM
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp=[[False]*len(s) for _ in range(len(s))]
        max_len=1
        start=0
        for i in range(len(s)):
            dp[i][i]=True
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                start=i
                max_len=2
        for l in range(3,len(s)+1):
            for i in range(len(s)-l+1):
                j=i+l-1
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j]=True
                    start=i
                    max_len=l
        return s[start:start+max_len]