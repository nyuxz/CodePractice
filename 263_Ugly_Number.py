# 263. Ugly Number

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        if num <= 0:
            return False
        
        if num == 1:
            return True
        
        for i in [2,3,5]:
            while num % i == 0:
                num = num/i
        
        if num == 1:
            return True
        else:
            return False


    def isUgly_2(self, num):
        """
        :type num: int
        :rtype: bool
        @logit: Recursion 
        """
        if num <= 0:

            return False
        if num == 1:
            return True

        if num % 2 == 0:
            return self.isUgly(num/2)
        elif num % 3 == 0:
            return self.isUgly(num/3)
        elif num % 5 == 0:
            return self.isUgly(num/5)
        else:
            return False