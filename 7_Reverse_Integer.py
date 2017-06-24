# 7. Reverse Integer

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0 :
            x = -x
            x = str(x)
            r = x[::-1]
            r = int(r)
            r = -r
        else:
            x = str(x)
            r = x[::-1]
            r = int(r)
        
        return r

print ((Solution()).reverse(-1234567))