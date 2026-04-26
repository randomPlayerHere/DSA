class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_sum = 0
        max_sum = float('-inf')
        for i in range(len(nums)):
            if local_sum <0:
                local_sum = 0
            local_sum += nums[i]
            max_sum = max(max_sum, local_sum)
        return max_sum