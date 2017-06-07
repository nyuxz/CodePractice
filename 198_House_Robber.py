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
        
        last, now = 0, 0
        
        for i in nums: 
            last, now = now, max(last + i, now)
                
        return now


if __name__ == '__main__':
    print (Solution().rob([8,4,8,5,9,6,5,4,4,10]))
    print (Solution().rob_2([8,4,8,5,9,6,5,4,4,10]))




