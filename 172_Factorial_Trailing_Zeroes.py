# 172. Factorial Trailing Zeroes
# https://leetcode.com/problems/factorial-trailing-zeroes/description/

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        @logic: Recursion
        	1. All traoling zeros are given by 2*5
        	2. there must be enough 2
        	3. basically we just count how many factor of 5 
        """
        return 0 if n == 0 else n / 5 + self.trailingZeroes(n / 5)


class Solution_2(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n > 0:
            n = n/5
            res += n
        return res