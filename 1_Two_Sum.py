# 1. Two Sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        @logit
        1. hash table (dictionary)
        2. the key point of using dict: value as dict-key and index as dict-value
        """
        if len(nums) < 1:
            return 'Error'
        
        dict = {}
        
        for i in range(len(nums)):
            
            x = nums[i]
            
            # condition on if index in dict 
            if target-x in dict:
                return (dict[target-x], i)
            else:
                dict[x] = i 