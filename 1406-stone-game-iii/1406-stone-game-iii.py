class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [-1] *n
        def recur(i):
            if i>=n:
                return 0
            if dp[i] !=-1:
                return dp[i]
            result = stoneValue[i] -recur(i+1)
            if i+1<n:
                result = max(result, stoneValue[i] + stoneValue[i+1] - recur(i+2))
            if i+2 <n:
                result = max(result, stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - recur(i+3))
            dp[i] = result
            return dp[i]
        answer = recur(0)
        if answer ==0:
            return "Tie"
        elif answer > 0:
            return 'Alice'
        else:
            return 'Bob'
        

            