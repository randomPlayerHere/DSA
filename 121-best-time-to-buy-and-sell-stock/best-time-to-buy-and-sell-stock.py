class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_stock = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            this_profit = prices[i] - min_stock
            profit = max(this_profit, profit)
            min_stock = min(min_stock, prices[i])
        return profit