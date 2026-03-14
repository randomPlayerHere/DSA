class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        def tabulation():
            dp = [[0]*2 for _ in range(n+1)]
            dp[n][0] = dp[n][1] = 0
            for i in range(n-1,-1,-1):
                for j in range(2):
                    if j==0:
                        dp[i][j] = max(-prices[i] + dp[i+1][1] ,dp[i+1][0])
                    else:
                        dp[i][j] = max(prices[i] + dp[i+1][0] ,dp[i+1][1])
            return dp[0][0]
        return tabulation()