# Last updated: 5/29/2026, 11:59:30 AM
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])

        def backtrack(x, y, index):

            if index == len(word):
                return True

            if (x < 0 or y < 0 or
                x >= rows or y >= cols or
                board[x][y] != word[index]):
                return False

            temp = board[x][y]
            board[x][y] = "#"

            found = (
                backtrack(x-1, y, index+1) or
                backtrack(x+1, y, index+1) or
                backtrack(x, y-1, index+1) or
                backtrack(x, y+1, index+1)
            )

            board[x][y] = temp

            return found

        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True

        return False