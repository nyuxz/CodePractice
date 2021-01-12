class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        # first DP, from left to right
        min_price = float('inf')
        total_max_price = 0
        
        first_profit = [0] * len(prices)
        
        for i in range(len(prices)):
            
            min_price = min(min_price, prices[i])
            first_profit[i] = max(first_profit[i-1], prices[i]-min_price)
            total_max_profit = first_profit[i]
            
    
        # second DP, from right to left
        max_price = float('-inf')
        second_max_profit = 0
        
        for i in range(len(prices)-1, 0, -1):
            max_price = max(prices[i], max_price)
            second_max_profit = max(second_max_profit, max_price - prices[i])
            
            total_max_profit = max(total_max_profit, first_profit[i-1]+second_max_profit)
        
        return total_max_profit
        