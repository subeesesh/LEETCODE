# Last updated: 5/29/2026, 11:55:40 AM
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        row=len(board)
        col=len(board[0])
        def dfs(i,j):
            if i<0 or j<0 or i>=row or j>=col or board[i][j]=='.':
                return 
            board[i][j]='.'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        count=0
        for i in range(row):
            for j in range(col):
                if board[i][j]=='X':
                    count+=1
                    dfs(i,j)
        return count
