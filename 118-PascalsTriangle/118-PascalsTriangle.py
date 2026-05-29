# Last updated: 5/29/2026, 11:58:44 AM
class Solution:
    def generate(self, numRows: int):
        triangle = []
        for i in range(numRows):
            row = [1] * (i + 1) 
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)

        return triangle
