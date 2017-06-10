# 121. Best Time to Buy and Sell Stock

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