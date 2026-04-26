class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        op_profit = float('-inf')
        for cur in prices:
            profit = cur-min_val
            op_profit = max(profit, op_profit)
            min_val = min(cur, min_val)
        return op_profit