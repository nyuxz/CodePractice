# 204. Count Primes

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        @logit:
        	1. Sieve of Eratosthenes -> https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithm_complexity
        """

        if n < 2: 
            return 0

        counterList = [1] * n
        counterList[0] = 0 # 0 is not prime
        counterList[1] = 0 # 1 is not prime

        for i in range(2, int(n**0.5)+1): # follow the algo, ToDo: Prove it
            if counterList[i] == 1:
                for j in range(2*i, n , i): # if i is prime, 2i, 3i, 4i..... will not be prime, so change conterList to zero
                    counterList [j] = 0

        return sum(counterList)