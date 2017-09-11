#26. Remove Duplicates from Sorted Array
#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        @logic: pointer go through
        """
        
        if len(nums) == 0:
            return 0
        
        pointer = 0 #initial pointer position
        for i in range(1, len(nums)):
            if nums[i] != nums[pointer]:
                pointer += 1
                nums[pointer] = nums[i]
            
        return pointer + 1 
            
        
