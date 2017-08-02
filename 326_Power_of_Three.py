# 326. Power of Three
# https://leetcode.com/problems/power-of-three/description/

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        @logic: brute force
        	1. Time Limit Exceeded
        """

        if n < 0: 
        	return False

        while n % 3 == 0:
        	n = n // 3 

        return n == 1 


class Solution_2(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        @logic: Recursion
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        if n%3 == 0:
            return self.isPowerOfThree(n/3)
        else:
            return False


class Solution_3(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        @logic: Limition
			1. signed integer, the maximum value of this data type is 2147483647
			2. 3^19 = 1162261467
        """

        # note: two conditions order is matter. if put n>0 at end, raising error.
        # coz, it will check first condition then second one. 
        return n > 0 and 1162261467 % n == 0 



