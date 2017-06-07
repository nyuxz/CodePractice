# 198. House Robber
class Solution(object):

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        @logit
        f(0) = nums[0]
        f(1) = max(num[0], num[1])
        f(k) = max( f(k-2) + nums[k], f(k-1) )
        """
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        # total_money_i_1 -> total money after robbed i-1's house
        total_money_i_1 = nums[0] 

        total_money_i = max(nums[0], nums[1])
        
        # i -> amount of money at ith house
        for i in nums[2:]:
            
            total_money_i_1, total_money_i_2 = total_money_i, total_money_i_1 
            total_money_i = max(total_money_i_1, total_money_i_2 + i)
            
        return total_money_i

    def rob_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        last, now = 0, 0
        
        for i in nums: 
            last, now = now, max(last + i, now)
                
        return now


    def rob_3(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        @logit: still using DP
        1. divide the house to even ids and odd ids
        2. find the max total money respectivelly
        """
        if len(nums) == 0:
            return 0
        
        total_even = 0
        total_odd = 0

        for i in range(0, len(nums)):

            if i % 2 == 0:
                total_even = max(total_even + nums[i], total_even)
                total_even = max(total_even, total_odd)
            
            elif i % 2 == 1:
                total_odd = max(total_odd + nums[i], total_odd)
                total_odd = max(total_odd, total_even)

        return max(total_odd, total_even)



if __name__ == '__main__':
    print (Solution().rob([8,4,8,5,9,6,5,4,4,10]))
    print (Solution().rob_2([8,4,8,5,9,6,5,4,4,10]))
    print (Solution().rob_3([8,4,8,5,9,6,5,4,4,10]))




