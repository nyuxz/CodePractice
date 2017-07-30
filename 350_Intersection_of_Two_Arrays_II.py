# 350. Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

import collections

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        @logic: list
        	1. comparing with question349, this shoud use list instead of dict
        """
        map_list = []
        intersect_list = []

        for i in nums1:
        	map_list.append(i)

        for j in nums2:
        	if j in map_list:
        		intersect_list.append(j)

        		map_list.remove(j)

       	return intersect_list


class Solution_2(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        @logic: Counter
        	1. list(collections.Counter(tmp)) will return list elements
			2. collections.Counter(tmp) will return <itertools.chain at 0x10f2a1f28>
        """
        return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())


if __name__ == '__main__':
	print (Solution().intersect([1,2,3,4,4], [4,4]))
	print (Solution_2().intersect([1,2,3,4,4], [4,4]))




