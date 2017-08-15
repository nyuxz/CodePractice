# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/description/

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        @note:
            1. similar question, 290. Word Pattern
        """
        return map(s.find, s) == map(t.find, t)

class Solution_2(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))