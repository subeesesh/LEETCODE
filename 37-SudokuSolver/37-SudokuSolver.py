# Last updated: 5/29/2026, 12:00:31 PM
class Solution:
    def solveSudoku(self, board):
        row=[set() for _ in range(9)]
        col=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num=board[i][j]
                row[i].add(num)
                col[j].add(num)
                boxes[(i//3)*3+j//3].add(num)
        def back():
            nonlocal board
            for i in range(9):
                for j in range(9):
                    if board[i][j]==".":
                        box_id=((i//3)*3+j//3)
                        for num in "123456789":
                            if num not in row[i] and num not in col[j] and num not in boxes[box_id]:
                                board[i][j]=num
                                row[i].add(num)
                                col[j].add(num)
                                boxes[box_id].add(num)
                                if back():
                                    return True
                                board[i][j]="."
                                row[i].remove(num)
                                col[j].remove(num)
                                boxes[box_id].remove(num)
                        return False
            return True
        back()