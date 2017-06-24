# 344. Reverse String

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
        



print (Solution().reverseString('abcdefg'))
print (Solution().reverseString_2('abcdefg'))