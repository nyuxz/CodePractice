# 389. Find the Difference
import collections

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        diff = list((collections.Counter(t) - collections.Counter(s)))

        return diff[0]


    def findTheDifference2(self, s, t):
    	ss = sorted(s)
    	tt = sorted(t)

    	diff = list(set(ss) - set(tt))

    	if diff == []:
    		diff = list(set(tt) - set(ss))

    	return diff[0]

print(Solution().findTheDifference("abcd", "abecd"))
print(Solution().findTheDifference2("abcd", "abcde"))