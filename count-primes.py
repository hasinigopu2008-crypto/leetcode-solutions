#my approach
#sieve of eratosthenes
class Solution(object):
    def countPrimes(self, n):
        if n<2:
            return 0
        isPrime=[True]*n
        isPrime[0]=isPrime[1]=False
        p=2
        while p*p<=n:
            if isPrime[p]:
                for multiple in range(p*p,n,p):
                    isPrime[multiple]=False
            p+=1
        return sum(isPrime)
#optimal approach
class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False
        for p in range(2, int(n**0.5) + 1):
            if isPrime[p]:
                num_elements = len(range(p * p, n, p))
                isPrime[p * p : n : p] = [False] * num_elements       
        return sum(isPrime)
