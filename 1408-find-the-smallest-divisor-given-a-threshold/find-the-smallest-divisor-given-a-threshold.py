class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def isValid(d):
            result = 0
            for i in range(len(nums)):
                result += -(nums[i]//-d)
            return result<= threshold
        low,high = 1, max(nums)
        result = 0
        while low<=high:
            mid = (low+high)//2
            if isValid(mid):
                result = mid
                high = mid-1
            else:
                low = mid+1
        return result
