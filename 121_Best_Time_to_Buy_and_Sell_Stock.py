# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0 
        min_price = float('inf')
        
        for stock in prices:
            
            min_price = min(min_price, stock)
            profit = stock - min_price
            
            max_profit = max(max_profit, profit)
            
        return max_profit


class Solution_2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        @logic: DP
        """
        if len(prices) == 0:
            return 0
        min_Price = prices[0]
        dp = [0] * len(prices)
        for i in range(0, len(prices)):
            dp[i] = max(dp[i-1], prices[i] - min_Price)
            min_Price = min(min_Price, prices[i])
        return dp[-1]