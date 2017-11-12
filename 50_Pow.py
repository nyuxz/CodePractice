# 50. Pow(x, n)
# https://leetcode.com/problems/powx-n/hints/

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        @logic: Recursion
            1. pow(x,n) = pow(x^2, n-1)
            2. O(log(n))
        """

        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)

        if n % 2 == 1 :
            return self.myPow(x, n-1) *x
        else:
            return self.myPow(x*x, n/2)

