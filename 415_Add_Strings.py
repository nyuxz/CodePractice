# 415. Add Strings

'''
Detial about question:

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

from itertools import zip_longest

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str

        @logit:
        1. convert string to integer, and put in a list in reverse order
        2. add two list based on integer position in the list. 
        3. using carry

        """

        # convert string to integers using built-in function ord (string --> ASCII --> integer)
        def convertInt(str_num):
            return ord(str_num) - ord('0')
        
        # map string to a integer list in reverse order
        num1, num2 = list(map(convertInt, num1[::-1])), list(map(convertInt, num2[::-1]))
        
        # for loop purpose 
        if len(num1)<len(num2):
            num1, num2 = num2, num1
        
       	# deal with carry    
        carry = 0
        for i in range(len(num1)):
            n = num2[i] if i<len(num2) else 0 
            tmp = n + carry + num1[i] 
            num1[i] = tmp % 10
            carry = tmp // 10
        
        if carry:
            num1.append(1)
        
        return ''.join(map(str, num1))[::-1]


    def addStrings_2(self, num1, num2):
    	'''
    	@logit: using itertools.zip_longest
    	1. izip_longest: combine items to tuple generator
    	2. still need reverse order of items list
    	'''
    	carry = 0 
    	result = '' # define result as a empty string

    	for (x, y) in zip_longest(num1[::-1], num2[::-1], fillvalue='0'):
    		tmp = (int(x) + int(y) + carry)
    		reminder = tmp % 10
    		carry = tmp // 10

            # add order is important
    		result = str(reminder) + result

    	if carry:
            result = str(carry) + result

    	return result

            
if __name__ == '__main__':
	print (Solution().addStrings('1456','934'))
	print (Solution().addStrings_2('1456','934'))


'''
P.s. ord built-in function
ord('string'): convert a string to ASCII(American Standard Code for Information Interchange) value
e.g. convert string '0' to interger 48
ord('0') = 48 
ord('4') = 52
ord('4') - ord('0') = 4

P.s.s
itertools.zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-

'''


