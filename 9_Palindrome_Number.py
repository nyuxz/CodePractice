# 9. Palindrome Number

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        @logit:
            1. convert x int to str
            2. reverse str
            3. convert string back to int

        @note:
            1. integers will not overflow in python
            because python integers have arbitrary precision
        """
        
        if x < 0:
            return False
        
        s = str(x)
        r = int(s[::-1])
        
        return r == x