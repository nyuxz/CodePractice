# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/description/

# this question is a good practice for indexing of the python list


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        @note: You may assume that nums1 has enough space 
            (size that is greater or equal to m + n) to hold additional elements from nums2
        """
        
        i = m-1
        j = n-1
        
        while i >=0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[i+j+1] = nums1[i]
                i = i-1
            else:
                nums1[i+j+1] = nums2[j]
                j = j-1
                
        nums1[:j+1] = nums2[:j+1]
        
            

            
        