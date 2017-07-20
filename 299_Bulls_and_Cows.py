# 299. Bulls and Cows

from collections import Counter

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        @logit:
            1. Two lengths are always equal. -> Make this question much easier.
        """
        
        s, g = Counter(secret), Counter(guess)
        
        a = sum(i == j for i, j in zip(secret, guess))
        
        return '%sA%sB' % (a, sum((s & g).values()) - a)


'''
P.s.
1. Intersection of two list: 
    list(set(a).intersection(b))
2. Union of two list
    list(set().union(a,b))
3. Substraction of two list
    list(set(a) - set(b))
'''
