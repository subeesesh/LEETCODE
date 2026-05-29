# Last updated: 5/29/2026, 11:59:59 AM
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        r=n
        c=n
        left=0
        top=0
        right=c-1
        bottom=r-1
        res=[[0]*n for _ in range(n)]
        a=1
        while(top<=bottom and left<=right):
            for i in range(left,right+1):
                res[top][i]=a
                a+=1
            top+=1
            for i in range(top,bottom+1):
                res[i][right]=a
                a+=1
            right-=1
            if(top<=bottom):
                for i in range(right,left-1,-1):
                    res[bottom][i]=a
                    a+=1
                bottom-=1
            if(left<=right):
                for i in range(bottom,top-1,-1):
                    res[i][left]=a
                    a+=1
                left+=1
        return res