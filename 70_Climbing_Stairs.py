# 70. Climbing Stairs

class Solution(object):
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        
        @logit: Fibonacci Sequence
        dp[x] = dp[x - 1] + dp[x - 2]
        
        @Runtime: 42 ms, which is not successful 
        """
        if n == 1 :
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
                
    
    def climbStairs_2(self, n):
        
        a = b = 1
        for x in range(2, n+1):
            a, b = b, a + b
        return b

print(Solution().climbStairs(10))
print(Solution().climbStairs_2(10))