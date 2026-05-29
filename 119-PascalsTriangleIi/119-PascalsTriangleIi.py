# Last updated: 5/29/2026, 11:58:40 AM
class Solution:
    def getRow(self, rowIndex: int):
        row = [1] * (rowIndex + 1)
        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                row[j] = row[j] + row[j - 1]
        return row
