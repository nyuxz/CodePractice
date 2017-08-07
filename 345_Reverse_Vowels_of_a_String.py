# 345. Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        @logic:
            1. find all vowels first and save to the list vowels
            2. go through string again and when find vowel then replace to vowels.pop() [reverse order to replace]
        @note:
            1. re.sub(pattern, replace-to, input-string)
            2.  (?i) makes it case-insensitive
            3. pop up last element of a list each time
        """
        import re
        
        vowels = re.findall('(?i)[aeiou]', s)
        
        '''
        *pay attention here*
        this is not same with following loop
        # for m in inverse(vowels):
        #   re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)
        which will be result as 'leetcede'
        '''
        result = re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)
        
        return result

class Solution_2(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        @logic:
            1. find all vowels and its position in string list
            2. reverse replace
        """
    
        strList = list(s)
        
        vowels = []
        for i in range(len(strList)):
            if strList[i] in ['a', 'o', 'e', 'i', 'u', 'A', 'O', 'E', 'I', 'U']:
                vowels.append([i, strList[i]])
                
        for j in range(len(vowels)/2):
            strList[vowels[j][0]] = vowels[len(vowels)-j-1][1]
            strList[vowels[len(vowels)-j-1][0]] = vowels[j][1]
        return ''.join(strList)

        