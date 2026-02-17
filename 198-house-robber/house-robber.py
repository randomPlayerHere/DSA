class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def tabulation():
            dp = [0] * n
            if n==0:
                return 0
            elif n==1:
                return nums[0]
            elif n==2:
                return max(nums)
            dp[0],dp[1] = nums[0], max(nums[0], nums[1])
            for i in range(2,n):
                not_rob = dp[i-1]
                rob = dp[i-2] + nums[i]
                dp[i] = max(rob, not_rob)
            return dp[n-1]
        return tabulation()

