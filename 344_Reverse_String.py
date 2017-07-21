# 344. Reverse String
import math 

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        @logit: slice
        """
        return s[::-1]

    def reverseString_2(self, s):

    	r = list(s)
    	r.reverse()
    	result = ''.join(r)
    	return result
        

    def reverseString_3(self, s):

    	result = ''.join(reversed(s))

    	return result

    def reverseString_4(self, s):
        '''
        @logit: Recursion
        '''
        if len(s) <= 1:
            return s

        left_s = s[:len(s)//2]
        right_s = s[len(s)//2:]
        return self.reverseString_4(right_s) + self.reverseString_4(left_s)

    def reverseString_5(self,s):
        '''
        @logit:
            1. this is the very traditional way to reverse a list/string/integer
            2. 暴力
        '''
        s = list(s)

        for i in range(0, len(s)//2):
            tmp = s[i]
            s[i] = s[len(s) -1 - i]
            s[len(s) -1 - i] = tmp

        return ''.join(s)


print (Solution().reverseString('abcdefg'))
print (Solution().reverseString_2('abcdefg'))
print (Solution().reverseString_3('abcdefg'))
print (Solution().reverseString_4('abcdefg'))
print (Solution().reverseString_5('abcdefg'))





