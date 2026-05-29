# Last updated: 5/29/2026, 11:55:20 AM
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row=len(mat)
        col=len(mat[0])
        q=deque()
        q.append((0,0))
        visited=set()
        visited.add((0,0))
        res=[]
        flag=True
        while q:
            size=len(q)
            level=[]
            for _ in range(size):
                r,c=q.popleft()
                level.append(mat[r][c])
                if c+1<col and (r,c+1) not in visited:
                    q.append((r,c+1))
                    visited.add((r,c+1))
                if r+1<row and (r+1,c) not in visited:
                    q.append((r+1,c))
                    visited.add((r+1,c))
            if not flag:
                res.extend(level)
            else:
                res.extend(level[::-1])
            flag=not flag
        return res
                