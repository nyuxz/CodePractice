# 66. Plus One
# https://leetcode.com/problems/plus-one/description/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        plus = 1
        
        for i in range(len(digits)-1, -1, -1):
            if digits[i] + plus > 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + plus
                plus = 0
        
        if plus == 1:
            digits.insert(0, 1)
            
        return digits