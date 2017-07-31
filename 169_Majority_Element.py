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


class Solution_2(object):
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


if __name__ == '__main__':
	print (Solution().majorityElement([4,4,4,4,5,5,5,5,5]))
