# 27. Remove Element
# https://leetcode.com/problems/remove-element/description/

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        @logic: delete multiple elements in a list at once
        @note: correct answer, but cannot AC
        """
        import numpy as np
        
        to_del_index = []
        for i in range(0,len(nums)):
            if nums[i] == val:
                to_del_index.append(i)
        
        new_nums = np.delete(nums, to_del_index).tolist()
        
        return len(new_nums)


class Solution_2(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[length] = nums[i]
                length += 1
        return length


if __name__ == '__main__':
 	print(Solution().removeElement([3,2,2,3],3))
 	print(Solution_2().removeElement([3,2,2,3],3))