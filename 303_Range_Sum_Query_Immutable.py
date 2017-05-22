# 303. Range Sum Query - Immutable

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sums = nums
        for i in range(1, len(nums)):
            self.sums[i] += self.sums[i-1]
        
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        result = self.sums[j] - (self.sums[i-1] if i > 0 else 0)
        return result
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray([-2,0,3,-5,2,-1])
# param_1 = obj.sumRange(2,5)

'''
note:
1. In sumRange function, it is impportant to check if i > 0 
'''

