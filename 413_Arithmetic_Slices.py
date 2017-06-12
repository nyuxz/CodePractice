#413. Arithmetic Slices

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        @logit: dp
        dp[i] save the number of slices at ith location
        """
        dp = [0] * len(A)
        count = 0
        
        for i in range(2, len(A)):
            if A[i-1] - A[i-2] == A[i] - A[i-1]:
                dp[i] = dp[i-1] + 1 
                
            count += dp[i]
        
        return count


print (Solution().numberOfArithmeticSlices([1,2,3,4,5,6]))