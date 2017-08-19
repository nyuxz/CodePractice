# 119. Pascal's Triangle II
# https://leetcode.com/problems/pascals-triangle-ii/


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        @logic: jth row = (j-1) row + (j-1) row's shift

        """
        row = [1]
        
        # _ is just a variable name, use _ for throwaway variables. 
		# It just indicates that the loop variable isn't actually used.
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])] # should put x+y result into a list
        return row