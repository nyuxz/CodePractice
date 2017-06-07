#53. Maximum Subarray

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        @Logit 
		Kadane's algorithm, O(n) complexity 
		state: lookup[i]
		dp: lookup[i] = max(A[i], A[i] + lookup[i-1])

        """
        currMax = nums[0]
        Max = nums[0]
        for i in nums[1:]:
        	currMax = max(i, currMax + i)
        	Max = max(Max, currMax)

        return Max


# testing
if __name__ == '__main__':
    print (Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))



'''
@Note 
1. without the dp, the complexity is O(n^2)
2. ToDo: divide and conquer approach, O(nlogn) 
'''