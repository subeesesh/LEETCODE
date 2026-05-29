# Last updated: 5/29/2026, 11:54:15 AM
class Solution:
    def primePalindrome(self, n: int) -> int:
        def isp(num):
            return str(num)==str(num)[::-1]
        def is_prime(n):
            if n<=1: return False
            if n==2: return True
            if n%2==0: return False
            for i in range(3,int(math.sqrt(n))+1,2):
                if n%i==0: return False
            return True
        while True:
            if isp(n) and is_prime(n):
                return n
            else:
                n+=1
            if 10**7<n<10**8:
                n=10**8
        return n


