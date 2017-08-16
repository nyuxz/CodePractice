# 118. Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        resList = [[1]] # resultList should be a list of list

        for i in range(1, numRows):

        	resList.append([]) # for each row, append a new list of list

        	for j in range(i+1):
        		left = resList[i-1][j-1] if j > 0 else 0
        		right = resList[i-1][j] if j < i else 0
        		resList[i].append(left + right)

        return resList



class Solution_2(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
		@note:
			1. jth row = (j-1) row + (j-1) row's shift
			2. e.g:
				    1 3 3 1 0 
				 +  0 1 3 3 1
				 =  1 4 6 4 1 
        """

        res = [[1]]
        for i in range(1, numRows):

        	'''
        	res is a list of list

        	res.append([list]) is equalent to 
        	res = res + [[list]] # atention: here should be a list of list
        						 # 加号左右两边的data structure should be same
        	'''

        	# res[-1] will always represent last row

        	currRow = list(map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1]))

        	res += [currRow]
        	#res.append(currRow)

        return res[:numRows]


if __name__ == '__main__':
	print (Solution().generate(5))
	print (Solution_2().generate(5))


'''
P.s

for i in range(1,1):
	print(i)

-> []

for i in range(1,2):
	print(i)

-> [1]

for i in range(2):
	print(i)

-> [0,1]

'''
