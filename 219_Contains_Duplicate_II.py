# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/description/

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        @logic:
            make up a dictionary, where number is the key and index is the value
        """
        index_dict = {}
        
        for i in range(len(nums)):
            
            if nums[i] in index_dict and i - index_dict[nums[i]] <= k:
                return True
            else:
                index_dict[nums[i]] = i 
                
        return False