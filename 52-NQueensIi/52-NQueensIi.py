# Last updated: 5/29/2026, 12:00:13 PM
class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        board=[["." for _ in range(n)] for _ in range(n)]
        count=0
        col=set()
        d1=set()
        d2=set()
        def backtrack(r):
            nonlocal count
            if(r==n):
                count+=1
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
        return count