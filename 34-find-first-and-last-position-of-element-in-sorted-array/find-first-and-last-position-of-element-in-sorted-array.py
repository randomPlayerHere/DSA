import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower_bound = bisect.bisect_left(nums, target)
        upper_bound = bisect.bisect_right(nums, target)
        if lower_bound == len(nums) or nums[lower_bound] != target:
            return [-1,-1]
        return [lower_bound, upper_bound-1]
        