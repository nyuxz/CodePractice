# 169_Majority_Element
# https://leetcode.com/problems/majority-element/description/


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        @logic: hashtable
        	1. There is only one number will be return, cannot be more than one
        	number count greater than half of the length of the list.
        	2. Stop once we find qualified number
			3. O(n)

        @note:
        	tmp = {}
        	tmp[1] = 'a'
			
			dict.get(key, initial) if key not exists in dict then return initial value
        	tmp.get(1,0) = 'a'
        	tnp.get(2,0) = 0
        """

        digits = {}
        for i in nums:
            digits[i] = digits.get(i, 0) + 1
            if digits[i] > len(nums)/2:
                return i


class Solution_2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distinct_nums = set(nums)
        for i in distinct_nums:
            if nums.count(i) > len(nums)/2:
                return i


class Solution_3(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        @logic: sort first 
        	1. sort the number list first
        	2. the middle number of the list must the majorit element
        	3. O(nlogn)
        """
        nums.sort()
        return nums[len(nums)/2]


class Solution_4(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        @logic: Randomization
        	1. pick a number from number_list randomly and count it
        	2. average query time must less than n/2
        	3. average complexity: O(n)

        """
        import random
        while True:
            r = random.choice(nums)
            if nums.count(r) > len(nums)/2:
                return r

class Solution_5(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        @logic: Divide and Conquer
            1. divide nums list to half and half and find majority from each half.
            2. if the majority of two half are same, this majority number will be the result.
            3. O(nlogn) where T(n) = T(n/2) + 2n
        """
        
        return self.majority(nums, 0, len(nums) - 1)
    
    def majority(self, nums, left_index, right_index):
        
        # for the case there is only one numbers in the list
        if left_index == right_index:
            return nums[left_index]
        
        mid_index = (left_index + right_index) / 2
        
        majority_left = self.majority(nums, left_index, mid_index)
        majority_right = self.majority(nums, mid_index+1, right_index)
        
        if majority_left == majority_right:
            return majority_left
        
        elif nums[left_index: right_index+1].count(majority_left) > nums[left_index: right_index+1].count(majority_right):
            return majority_left

        else:
            return majority_right


class Solution_6(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        @logic: Moore Voting Algorithm
            1. find a pair of different numbers and delete them it from nums list
            2. untill there is only same number left, this number will be the majority
            3. use count variable to record total count of marjority, and count number will offset with non-marjority numebrs. [nice]
        """
        major = count = 0
        for i in nums:
            if count == 0:
                major = i
                count = 1
            else:
                count += 1 if major == i else -1
        return major



'''
ToDo: solution_7: Bit Manipulation 
'''

if __name__ == '__main__':
	print (Solution().majorityElement([4,4,4,4,5,5,5,5,5]))
