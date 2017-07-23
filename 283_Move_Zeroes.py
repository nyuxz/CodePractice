# 283. Move Zeroes

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        @logit:
   			1. move all the non-zero number to the front of nums 
   			2. set all the tail number where dont have a num value to zero
        """

        i = 0
        for num in nums:
        	if num != 0:
        		nums[i] = num
        		i += 1

        for j in range(i, len(nums)):
        	nums[j] = 0


    def moveZeroes_2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        @logit:
        	1. loop all the number [from the tail to front]
			2. if find zero, move zero to the tail 
			and all the values after this zero will move one position forward together
        """

        for i in range(len(nums)-1, -1, -1): # standard way to loop from tail to front position
        	if nums[i] == 0:
        		for j in range(i+1, len(nums)): 
        			# move every number after zero one position forward
        			if nums[j] != 0:
        				nums[j-1] = nums[j]
        				nums[j] = 0


