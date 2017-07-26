# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/#/description

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        @logic:
            1. sort the list first
            2. for each element, comparing with its following numbers
            3. time: 52ms
        """
        
        nums.sort()
        # nums = sorted(nums)
        
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

class Solution_2(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        @logic: Hashtable/Dictionary 
    		1. time: 69ms
    		2. instead of using dict, using list will rasie 'Time Limit Exceeded'
        """
        
        # list =[] too slow
        hashMap = {}
        
        for num in nums:
            if num in hashMap:
                return True
            hashMap[num] = True
        
        return False

class Solution_3(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))


        