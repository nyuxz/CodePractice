# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/description/

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        roman_map = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        res = 0
        tmp = 1

        # Scan roman number from end to first
        for i in range(len(s)-1, -1 , -1):

            if roman_map[s[i]] >= tmp:
                res += roman_map[s[i]]
                tmp = roman_map[s[i]]
            else:
                res -= roman_map[s[i]]

        return res


if __name__ == '__main__':
    print(Solution().romanToInt('XI'))








'''
P.s.
A brief intro of Roman
I（1）、X（10）、C（100）、M（1000）、V（5）、L（50）、D（500）

Roman	Integer		Roman	Integer
I	1				XXIX	29
II	2				XXX	30
III	3				XL	40
IV	4				L	50
V	5				LX	60
VI	6				LXX	70
VII	7				LXXX	80
VIII	8			XC	90 
IX	9				XCIX	99
X	10				C	100
XI	11				CI	101
XII	12				CXCIX	199
XIII	13			CC	200
XIV	14				CCC	300
XV	15				CD	400
XVI	16				D	500
XVII	17			DCLXVI	666
XVIII	18			M	1,000
XIX	19				MCMXCIX	1,999
XX	20				MM	2,000
XXI	21				MMM	3,000
XXII	22			MMMM	4,000
'''