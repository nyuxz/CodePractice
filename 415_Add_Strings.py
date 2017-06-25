# 415. Add Strings

'''
'12345' + '6780'

  12345
+  6780
--------
  19125 
  
also we can reverse the string following,

54321
0876 +
------
52191
'''

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def convertInt(str_num):
            return ord(str_num) - ord('0')
            
        num1, num2 = list(map(convertInt, num1[::-1])), list(map(convertInt, num2[::-1]))
        
        if len(num1)<len(num2):
            num1, num2 = num2, num1
            
        carry = 0
        for i in range(len(num1)):
            n = num2[i] if i<len(num2) else 0 
            tmp = n + carry + num1[i] 
            num1[i] = tmp % 10
            carry = tmp // 10
        
        if carry:
            num1.append(1)
        
        return ''.join(map(str, num1))[::-1]
            
if __name__ == '__main__':
	print (Solution().addStrings('1456','934'))


'''
P.s. ord built-in function
ord('string'): convert a string to ASCII(American Standard Code for Information Interchange) value
e.g. convert string '0' to interger 48
ord('0') = 48 
ord('52') = 52
ord('4') - ord('0') = 4
'''