class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        def tabulation():
            dp = [[0]*(n+1) for _ in range(n+1)]
            # dp[n][*] = 0
            for i in range(n-1,-1,-1):
                for j in range(i,-1,-1):
                    take = 0
                    not_take = dp[i+1][j]
                    if j==0 or nums[i] % nums[j-1] ==0:
                        take = 1 + dp[i+1][i+1]
                    dp[i][j] = max(take, not_take)
            i,j = 0,0
            result = []
            while i<n:
                if dp[i][j] == dp[i+1][j]:
                    i+=1
                else:
                    result.append(nums[i])
                    j=i+1
                    i+=1
            return result
        return tabulation()