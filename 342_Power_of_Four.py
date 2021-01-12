# 342_Power_of_Four
# https://leetcode.com/problems/power-of-four/description/

class Solution(object):

    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1:
            return True
        if num%4 == 0:
            return self.isPowerOfFour(num/4)
        else:
            return False


'''
ToDo: binary 
'''