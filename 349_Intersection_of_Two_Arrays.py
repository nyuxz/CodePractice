# 349. Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/tabs/description

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))


class Solution_2(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        @logic: 暴力
        """
        intersection = []
        
        for i in nums1:
            if i in nums2 and i not in intersection:
                intersection.append(i)
                
        return intersection


class Solution_3(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        @logic: dict
            1. the benifit: dict will never double count same [key, value]
            e.g. dict[a] = 1 -> {a:1}
            if we add another same key and value dict[a] = 1, the dict keep same as {a:1}
            however, if the list, will keep append whenever same elements or not
        """
        itec_dict = {}
        map_dict = {}

        for i in nums1:
        	map_dict[i] = 1
    
        for j in nums2:
        	if j in map_dict:
        		itec_dict[j] = 1
                
        return list(itec_dict.keys())

