# 28. Implement strStr()
# https://leetcode.com/problems/implement-strstr/description/

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        @note:
        	if finded, return 0 otherwise return 1
        """
        return haystack.find(needle)


class Solution_2(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        
        return -1
        