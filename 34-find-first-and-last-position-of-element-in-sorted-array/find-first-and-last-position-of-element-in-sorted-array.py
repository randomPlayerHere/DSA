import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = bisect.bisect_left(nums, target), bisect.bisect_right(nums, target)
        if start ==end:
            return [-1,-1]
        else:
            return [start, end-1]


        