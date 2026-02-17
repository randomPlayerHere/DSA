class Solution:
    def rob(self, nums: List[int]) -> int:
        def tabulation(a):
            n = len(a)
            if n==0:
                return 0
            elif n==1:
                return a[0]
            elif n==2:
                return max(a)
            dp = [0] * n
            dp[0],dp[1] = a[0], max(a[0], a[1])
            for i in range(2,n):
                rob = dp[i-2] + a[i]
                not_rob = dp[i-1]
                dp[i] = max(rob, not_rob)
            return dp[n-1]
        if len(nums) == 1:
            return nums[0]
        return max(tabulation(nums[1:]), tabulation(nums[:-1]))
