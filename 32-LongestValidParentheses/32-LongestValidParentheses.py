# Last updated: 5/29/2026, 12:00:43 PM
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[-1]
        maxlen=0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxlen=max(maxlen,i-stack[-1])
        return maxlen