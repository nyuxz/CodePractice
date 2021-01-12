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
        @logic: DP
        """
        if len(prices) == 0: 
            return 0
        
        min_price = prices[0]
        max_profit = [0] * len(prices)
        
        for i in range(0, len(prices)):
            
            min_price = min(prices[i], min_price)
            max_profit[i] = max(max_profit[i-1], prices[i]-min_price)
            
            
        return max_profit[-1]

