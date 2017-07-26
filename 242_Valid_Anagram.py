# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/#/description
# Anagram: 词的字母变化后组成的新词

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        ord_s_sum = 0
        ord_t_sum = 0 
        for i in s:
            ord_s_sum += ord(i)
            
        for j in t:
            ord_t_sum += ord(j)
        
        return ord_s_sum == ord_t_sum and set(s) == set(t)

class Solution_2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """     
        return sorted(list(s)) == sorted(list(t))


