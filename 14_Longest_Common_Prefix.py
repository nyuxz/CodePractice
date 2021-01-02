# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/description/


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        @note:
        	1. zip() fuinction in python
        		e.g. strs = ['123','456','6789']
					 list(zip(strs))
					 [('123',), ('456',), ('6789',)]
					 list(zip(*strs))
					 ('1', '4', '6'), ('2', '5', '7'), ('3', '6', '8')]

			2. enumerate() in python
				e.g. for i, j in enumerate(zip(*strs)): print(i,j)
				     0 ('1', '4', '6')
					 1 ('2', '5', '7')
					 2 ('3', '6', '8')
        """

        if not strs:
            return ""
        
        for i, chars in enumerate(zip(*strs)):
            
            if i == 0 and len(set(chars)) > 1:
                return ""
                
            if len(set(chars)) > 1:
                return strs[0][:i]
        
        # If only one string in strs list
        return min(strs)
