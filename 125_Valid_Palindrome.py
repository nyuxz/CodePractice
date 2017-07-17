#125. Valid Palindrome

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        @logit:
        	1. isalnum() returns a Boolean tell whether the string contains only letters and digits.
        """

        # this cleanlist only contains only letters and digits 
        cleanlist = [c for c in s.lower() if c.isalnum()]
        
        return cleanlist == cleanlist[::-1]



    def isPalindrome_2(self, s):
        """
        :type s: str
        :rtype: bool
        @logit:
            1. parsing evey digital and letter to a list
            2. check if a list is palindorme
                for i in range(0, len(list)/2):
                    if list[i] != list[length-i-1]
        """

        cleanlist = []
        for c in s.lower():
            if c.isalnum():
                cleanlist.append(c)

        length = len(cleanlist)
        for i in range(0, length/2):
            if cleanlist[i] != cleanlist[length-i-1]:
                return False
        return True