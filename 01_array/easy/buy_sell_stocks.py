class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        profit = 0
        curr = prices[0]
        for i in range(len(prices)):
            if prices[i] < curr:
                curr = prices[i]
            profit = max(profit, prices[i] - curr)
        return profit