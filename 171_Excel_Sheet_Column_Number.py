# 171. Excel Sheet Column Number
# https://leetcode.com/problems/excel-sheet-column-number/#/description

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        @logic: 
        	1. 2 = ord('B') - 64
        """
        sum = 0
        for c in s:
        	# 每逢26进1位
            sum = sum*26 + (ord(c) - 64) # 64 = ord('A') - 1
        return sum


class Solution_2(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        @logic: 
        	1. map(function, list)
        	2. reduce(function, iterable, initializer=None)
        	
        @note:
        	for example s = 'ABC'

        	map(lambda x:ord(x)-64, 'AB') -> [1,2]

        	reduce(lambda x,y: x*26 + y, [1,2], 0) -> reduce(lambda x,y: x*26 + y, [0,1,2])
        		step1: x,y = 0,1 -> 0*26+1=27
        		step2: x,y = 1,2 -> 1*26+2=28

        	therefore, 'AB' -> 28

        """
        return reduce(lambda x,y: x*26 + y, map(lambda x:ord(x)-64, s), 0)


'''
P.s.

def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value
'''

