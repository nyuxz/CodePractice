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

    	r = list(s) # parsing a string
        r.reverse() # reverse
        result = ''.join(r) # combine a list items to a string

        return result
