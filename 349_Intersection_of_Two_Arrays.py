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
        """
        intersection = []
        
        for i in nums1:
            if i in nums2 and i not in intersection:
                intersection.append(i)
                
        return intersection