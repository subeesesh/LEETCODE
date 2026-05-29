# Last updated: 5/29/2026, 11:56:16 AM
from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str):
        def isValid(st):
            count = 0
            for ch in st:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        res = []
        visited = set([s])
        queue = deque([s])
        found = False

        while queue:
            curr = queue.popleft()

            if isValid(curr):
                res.append(curr)
                found = True

            if found:
                continue

            for i in range(len(curr)):
                if curr[i] not in ('(', ')'):
                    continue
                nxt = curr[:i] + curr[i+1:]
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)

        return res
