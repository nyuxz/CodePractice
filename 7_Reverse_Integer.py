# 7. Reverse Integer

class Solution(object):
    def reverse(self, x):
        """
        '''
        1. range of the 32bit integer
        2. after reverse the integer start with 0
        3. negative integers
        '''
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


    def reverse_2(self, x):
        """
        :type x: int
        :rtype: int
        @note: handle overflow
        """
        if x < 0:
            return -self.reverse(-x)

        result = 0
        while x:
            result = result * 10 + x % 10
            x /= 10
        return result if result <= 0x7fffffff else 0  # Handle overflow


if __name__ == "__main__":

    # reverse of 1000000003 overflows
    print((Solution()).reverse(1000000003))
    print((Solution()).reverse_2(1000000003))


'''
ToDo: what is overflows
'''