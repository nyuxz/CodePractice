# 168. Excel Sheet Column Title
# https://leetcode.com/problems/excel-sheet-column-title/#/description

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        title = ''
        
        while n != 0:
            title = chr((n-1)%26 +65) + title
            n = (n-1)/26
        
        return title


class Solution_2(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        @logic: Recurrsion
        	1. [if n==0: return ''] cannot ignore
        """
        
        if n == 0: 
            return ''
        
        title = ''
        
        title = chr((n-1)%26 +65)
        n = (n-1)/26
        
        return self.convertToTitle(n) + title