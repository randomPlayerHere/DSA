class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        k_cap = k
        n = len(prices)
        def recur(ind, ib, cap):
            if cap==0 or ind ==n:
                return 0
            if ib==0:
                profit = max(-prices[ind] + recur(ind+1, 1, cap), recur(ind+1, 0, cap))
            else:
                profit = max(prices[ind] + recur(ind+1, 0, cap-1), recur(ind+1, 1, cap))
            return profit
        # return recur(0,0,k)
        def tabulation():
            dp = [[[0 for _ in range(k_cap+1)]for _ in range(2)]for _ in range(n+1)]
            for i in range(n-1,-1,-1):
                for j in range(2):
                    for k in range(1,k_cap+1):
                        if j==0:
                            dp[i][j][k] = max(-prices[i] + dp[i+1][1][k], dp[i+1][0][k])
                        else:
                            dp[i][j][k] = max(prices[i] + dp[i+1][0][k-1], dp[i+1][1][k])
            return dp[0][0][k_cap]
        return tabulation()

