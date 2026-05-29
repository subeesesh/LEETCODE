# Last updated: 5/29/2026, 11:57:05 AM
class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        num=0
        res=0
        sign=1
        for c in s:
            if c.isdigit():
                num=num*10+int(c)
            elif c=='+':
                res+=sign*num
                num=0
                sign=1
            elif c=='-':
                res+=sign*num
                num=0
                sign=-1
            elif c=='(':
                stack.append(res)
                stack.append(sign)
                res=0
                sign=1
            elif c==')':
                res+=sign*num
                num=0
                res*=stack[-1]
                stack.pop()
                res+=stack[-1]
                stack.pop()
        res+=sign*num
        return res