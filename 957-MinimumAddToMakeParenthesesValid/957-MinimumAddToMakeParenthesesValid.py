# Last updated: 5/29/2026, 11:54:03 AM
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        for i in s:
            if i=='(':
                stack.append(i)
            else:
                if stack and stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(i)
        return len(stack)