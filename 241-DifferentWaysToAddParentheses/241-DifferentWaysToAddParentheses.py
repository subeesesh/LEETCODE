# Last updated: 5/29/2026, 11:56:44 AM
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operations={
            "+":lambda x,y:x+y,
            "-":lambda x,y:x-y,
            "*":lambda x,y:x*y
        }
        def back(left,right):
            res=[]
            for i in range(left,right+1):
                op=expression[i]
                if op in operations:
                    nums1=back(left,i-1)
                    nums2=back(i+1,right)
                    for i in nums1:
                        for j in nums2:
                            res.append(operations[op](i,j))
            if res==[]:
                res.append(int(expression[left:right+1]))
            return res
        return back(0,len(expression)-1)