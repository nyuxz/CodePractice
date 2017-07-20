# 231. Power of Two

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n < 1: 
            return False
        
        while n % 2 == 0:
            n = n/2
            
        if n == 1:
            return True
        else:
            return False 