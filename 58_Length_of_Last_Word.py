# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/description/

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # str.rstrip() get out of empty space at the end of the string
        # str.split(' ') split the words by space
        return len(s.rstrip().split(' ')[-1])



class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        @logic: 
        	1. delete the space in the end of string
        	2. from end to head, count for non-space letters
        @note:
        	1. one space count for one length
        """

        length = 0 
        j = len(s)-1 # where len(s)-1 represent the position of the last letter 
        
        # delete tail space, at record non-space letter position
        while j>=0:
            if s[j] != ' ':
                break
            j = j - 1
         
        # count for last non-space word   
        for i in range(j, -1, -1): # range from end to head
            if s[i] == ' ':
                return length
            else:
                length = length + 1
                
        return length


