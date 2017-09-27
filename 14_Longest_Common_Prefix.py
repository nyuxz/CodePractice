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
            return ''

        for i, chars in enumerate(zip(*strs)):
            if len(set(chars)) > 1:
                return strs[0][:i]
        return min(strs)


class Solution_2(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        
        prefix = ''
        
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix

        