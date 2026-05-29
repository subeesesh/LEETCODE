# Last updated: 5/29/2026, 11:58:35 AM
class Solution(object):
    def isPalindrome(self, s):
        str1=""
        s1=s.lower()
        for i in s1:
            if i.isalnum():
                str1=str1+i
        if(str1==str1[::-1]):
            return True
        else:
            return False