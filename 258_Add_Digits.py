# 258. Add Digits

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        @note:
            1. 123 % 10 = 3
            2. 123 // 10 = 12
		@logit:
			1. straightforward, O(n)
        """
   
        if num <= 9:
            return num

        sum = 0
        while num > 9:

            sum = sum + num%10
            num = num /10
            
            if num >= 1 and num<=9:
                sum = sum + num
                num = sum
                sum = 0 #reset sum
            
        return num
            
    def addDigits_2(self, num):
        """
        :type num: int
        :rtype: int
        @logit: digit root problem
        	1. from 1 to 100, the result is [1,2,3,4,5,6,7,8,9] loop ever and ever again
        	2. dr(n) = 0, if n = 0 
        	   dr(n) = 9, if n != 0 and n mod 9 == 0 
        	   dr(n) = n mod 9, if n mod 9 != 0 
        """
        
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9
        
