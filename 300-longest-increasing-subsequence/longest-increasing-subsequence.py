class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # def recur(i, prev):
        #     if i==n:
        #         return 0
        #     take = 0
        #     not_take = recur(i+1,prev)
        #     if (prev==-1 or nums[i]>nums[prev]):
        #         take = 1 + recur(i+1, i)
        #     return max(take, not_take)
        # return recur(0,-1)
        dp = [[None]*(n) for _ in range(n)]
        def memo(i, prev):
            if i==n:
                return 0
            if dp[i][prev] is not None:
                return dp[i][prev]
            take = 0
            not_take = memo(i+1,prev)
            if (prev==-1 or nums[i]>nums[prev]):
                take = 1 + memo(i+1, i)
            dp[i][prev] = max(take, not_take)
            return dp[i][prev]
        return memo(0,-1)