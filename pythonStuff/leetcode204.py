from math import isqrt

class Solution:
    def countPrimes(self, n: int) -> int:
        #Solution uses the sieve of Eratosthenes
        #Creates an array composed of bools, all true to begin with
        #Works by going to each number 2-10 and marking down the multiples of that number as false(not prime)
        if n <= 2:
            return 0
        primes = [True] * n
        primes[0], primes[1] = False, False
        i = 2

        while i**2 <= n:
            if primes[i]:
                for x in range(i*i, n, i):
                    primes[x] = False
            i+= 1
        return primes.count(True)

print(Solution.countPrimes(Solution, 10))