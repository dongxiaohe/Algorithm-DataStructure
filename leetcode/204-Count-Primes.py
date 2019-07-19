class Solution(object):
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                j = 2
                while i * j < n:
                    primes[i * j] = False
                    j += 1
        return sum(primes)
