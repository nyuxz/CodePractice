#292. Nim Game

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        @logit:
            1. strategy: the one with 4 remaining must loose
            # if n == 4k, then at each round B can make A+B both take 4, 
            # eventually leave 4 to A, A lose
            # if n == 4k + i (i <= 3), then A can always take i first and B will
        """

        return bool(n%4!=0)
        

