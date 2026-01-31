import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # def recur(i,prev):
        #     if i<0:
        #         return 0
        #     take = 0
        #     not_take = recur(i-1,prev)
        #     if prev==-1 or nums[prev]>nums[i]:
        #         take = 1+recur(i-1,i)
        #     return max(take, not_take)
        # return recur(n-1, -1)
        # dp = [[None]*(n+1) for _ in range(n+1)]
        # def memo(i,prev):
        #     if i<0:
        #         return 0
        #     if dp[i+1][prev+1] is not None:
        #         return dp[i+1][prev+1]
        #     take = 0
        #     not_take = memo(i-1,prev)
        #     if prev==-1 or nums[prev]>nums[i]:
        #         take = 1 + memo(i-1,i)
        #     dp[i+1][prev+1] = max(take,not_take)
        #     return dp[i+1][prev+1]
        # return memo(n-1,-1)
        # def tabulation():
        #     dp = [[0]*(n+1) for _ in range(n+1)]
        #     for i in range(0,n):
        #         for j in range(-1, i):
        #             take = 0
        #             not_take = dp[i][j+1]
        #             if j==-1 or nums[j]>nums[i]:
        #                 take = 1+dp[i][i+1]
        #             dp[i+1][j+1] = max(take, not_take)
        #     return dp[n][0]
        # return tabulation()

        def bs():
            temp = []
            temp.append(nums[0])
            for i in range(1,n):
                if nums[i]>temp[-1]:
                    temp.append(nums[i])
                else:
                    ind = bisect.bisect_left(temp,nums[i])
                    temp[ind] = nums[i]
            return len(temp)
        return bs()