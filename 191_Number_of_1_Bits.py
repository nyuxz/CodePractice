# 191. Number of 1 Bits

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')


    def hammingWeight_2(self, n ):
    	'''
    	@logit:
    		1. Python's bitwise operators
    		2. x >> y: returns x with the bits shifted to the right by y places.
    		3. x & y: a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
    	'''

    	count = 0

    	while n: 
    		count += n&1 # if n is 1 then count plus 1
    		n >>= 1 # n = n>>1, n shift 1 

    	return count



    def hammingWeight_3(self, n):
    	'''
    	@logit:
    		1. n = n&(n-1) change all 1 to 0 
    		2. the time of loop is the number of 1
    	'''

        count = 0

        while n:
            count += 1
            n &= n-1
        return count