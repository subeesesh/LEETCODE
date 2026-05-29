# Last updated: 5/29/2026, 11:59:50 AM
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def length(arr):
            return len(" ".join(arr))
        def slen(arr):
            count=0
            for i in arr:
                count+=len(i)
            return count
        res=[]
        sen=[]
        count=0
        for i in words:
            if length(sen+[i])>maxWidth:
                len_sp=slen(sen)
                space_need=maxWidth-len_sp
                gap=len(sen)-1
                if gap==0:
                    res.append(sen[0]+" "*space_need)
                else:
                    k=space_need//gap
                    extra=space_need%gap
                    temp=""
                    for j in range(gap):
                        temp+=sen[j]
                        if j<extra:
                            temp+=" "*(k+1)
                        else:
                            temp+=" "*k
                    temp+=sen[-1]
                    res.append(temp)
                sen.clear()
            sen.append(i)
        last=" ".join(sen)
        last+=" "*(maxWidth-len(last))
        res.append(last)
        return res