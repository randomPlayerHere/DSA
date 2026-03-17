class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        def recur(ind, ib):
            if ind>=n:
                return 0
            if ib ==0:
                profit = max(-prices[ind] + recur(ind+1, 1), recur(ind+1, 0))
            else:
                profit = max(prices[ind] + recur(ind+2, 0), recur(ind+1, 1))
            return profit
        # return recur(0,0)
        def tabulation():
            dp = [[0] *2 for _ in range(n+2)]
            # by defaut the case case is satified during the dp defination
            for i in range(n-1, -1, -1):
                for j in range(2):
                    if j ==0:
                        dp[i][j] = max(-prices[i] + dp[i+1][1], dp[i+1][j])
                    else:
                        dp[i][j] = max(prices[i] + dp[i+2][0], dp[i+1][j])
            return dp[0][0]
        return tabulation()