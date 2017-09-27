# 67. Add Binary
# https://leetcode.com/problems/add-binary/description/

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        @logic:
        	1. int(a,2) convert a binary number to integer
        	2. bin(a) convert a interger to binary number
        	3. bin(a)[2:] take specific binary number out
        		e.g.
        			bin(15) ---> 0b1111
        			bin(15)[2:] --> 1111
        """
        return bin(int(a, 2) + int(b, 2))[2:]


class Solution_2(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        @logic: Recursion
            1. a[:-1] takes the string except last character  
        """

        if not a or not b:
            return a if a else b

        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'

        elif a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
            
        else:
            return self.addBinary(a[:-1], b[:-1]) + '1'


