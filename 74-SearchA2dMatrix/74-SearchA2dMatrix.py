# Last updated: 5/29/2026, 11:59:39 AM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        left=0
        right=m*n-1
        while(left<=right):
            mid=(left+right)//2
            midv=matrix[mid//n][mid%n]
            if midv==target:
                return True
            elif midv<target:
                left=mid+1
            else:
                right=mid-1
        return False