# Last updated: 5/29/2026, 11:51:19 AM
class Solution:
    def largestPrime(self, n: int) -> int:
        isPrime=[True]* (n+1)
        isPrime[0]=isPrime[1]=False
        for i in range(2,int((n**0.5))+1):
            if isPrime[i]:
                for j in range(i*i,n+1,i):
                    isPrime[j]=False
        primes=[]
        for i in range(2,n+1):
            if isPrime[i]:
                primes.append(i)
        sum=0
        maxx=0
        for p in primes:
            sum+=p
            if sum>n:
                break
            if isPrime[sum]:
                maxx=sum
        return maxx