# Last updated: 5/29/2026, 12:01:07 PM
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        n=len(digits)
        if n==0:
            return res
        map={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        def back(digits,s,i):
            if i==len(digits):
                res.append(s)
                return
            string=map[digits[i]]
            for j in string:
                s+=j
                back(digits,s,i+1)
                s=s[:-1]
        path=""
        back(digits,path,0)
        return res
             
            
