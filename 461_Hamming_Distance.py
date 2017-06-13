# 461. Hamming Distance

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        
        @logit
        1.convert number to binary number 
        2.count difference of two string
        """
        
        # convert a number to binary 8 string
        bin8 = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(2^31)] ) )
        
        xx = bin8(x)
        yy = bin8(y)
        
        # count the difference of two string
        diff = 0 
        u = zip(xx, yy)
        for i,j in u:
            if i != j:
                diff += 1
                
        return diff

    def hammingDistance2(self, x, y):
        '''
        @logit: ToDo
        '''

        return bin(x^y).count('1')
        
print (Solution().hammingDistance(12345, 67890))
print (Solution().hammingDistance2(12345, 67890))


'''
Note: To Do
Operaters: >>, &
'''






