# 12. Integer to Roman
# https://leetcode.com/problems/integer-to-roman/description/


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        @logic
        	1. CM = M - C = 1000 - 100 = 900
        """
    	values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    	numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    	list = ''
        for i in range(0, len(values)):
            while num >= values[i]:
                num -= values[i]
                list += numerals[i]
        return list



class Solution_2(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        @logic: Recursion
       	@note:
       		1. ToDo
       		2. not AC
        """

        roman_map = {1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}


        if len(str(num)) == 1:
        	return roman_map[num]

        digit = 10**(len(str(num))-1) # 10*2 = 100
        first_int = num // digit  # 321 // 100 = 3

        first_roman = roman_map[digit] * first_int

        if num % digit == 0:
       		return num
       	else:
       		num == num % digit

        return first_roman + self.intToRoman(num)

