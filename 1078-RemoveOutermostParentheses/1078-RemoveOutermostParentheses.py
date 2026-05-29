# Last updated: 5/29/2026, 11:53:39 AM
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        res = ""
        for ch in s:
            if ch == '(':
                if count > 0:
                    res += ch
                count += 1
            else:  
                count -= 1
                if count > 0:
                    res += ch

        return res
