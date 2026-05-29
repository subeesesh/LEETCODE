# Last updated: 5/29/2026, 11:57:27 AM
class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        def help(x):
            if x==1:
                return True
            if x in seen:
                return False
            seen.add(x)
            total=0
            while x>0:
                dig=x%10
                total+=dig*dig
                x=x//10
            return help(total)
        return help(n)
