# Last updated: 5/29/2026, 12:00:15 PM
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["." for _ in range(n)] for _ in range(n)]
        res=[]
        col=set()
        d1=set()
        d2=set()
        def backtrack(r):
            if(r==n):
                res.append(["".join(row)for row in board])
                return
            for c in range(n):
                if c in col or (r-c) in d1 or (r+c) in d2:
                    continue
                board[r][c]="Q"
                col.add(c)
                d1.add(r-c)
                d2.add(r+c)
                backtrack(r+1)
                board[r][c]="."
                col.remove(c)
                d1.remove(r-c)
                d2.remove(r+c)
        backtrack(0)
        return res