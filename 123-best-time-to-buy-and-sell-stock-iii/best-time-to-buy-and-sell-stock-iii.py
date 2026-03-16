class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        def recur(ind, ib, cap):
            if cap == 0 or ind==n:
                return 0
            if ib ==0:
                profit = max(-prices[ind] + recur(ind+1, 1, cap), recur(ind+1, 0, cap))
            else:
                profit = max(prices[ind] + recur(ind+1, 0, cap-1), recur(ind+1, 1, cap))
            return profit
        # return recur(0,0,2)

        def tabulation():
            dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n+1)]
            # base case already satisifed due to the defination
            for i in range(n-1, -1, -1):
                for j in range(2):
                    for k in range(1,3):
                        if j ==0:
                            profit = max(-prices[i] + dp[i+1][1][k], dp[i+1][0][k])
                        else:
                            profit = max(prices[i] + dp[i+1][0][k-1], dp[i+1][1][k])
                        dp[i][j][k] = profit
            return dp[0][0][2]
        # return tabulation()

        def space_optimized():
            right_i = [[0 for _ in range(3)] for _ in range(2)]
            curr_i = [[0 for _ in range(3)] for _ in range(2)]
            for i in range(n-1, -1, -1):
                for j in range(2):
                    for k in range(1,3):
                        if j ==0:
                            curr_i[j][k]= max(-prices[i] + right_i[1][k], right_i[0][k])
                        else:
                            curr_i[j][k]= max(prices[i] + right_i[0][k-1], right_i[1][k])
                right_i = curr_i
            return right_i[0][2]
        return space_optimized()


