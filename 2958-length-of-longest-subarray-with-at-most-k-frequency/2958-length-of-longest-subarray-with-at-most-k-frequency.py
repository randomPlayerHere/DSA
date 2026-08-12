class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        result = 0
        mp = {}
        l = 0
        for r in range(len(nums)):
            mp[nums[r]] = mp.get(nums[r],0) +1
            while mp[nums[r]] >k:
                mp[nums[l]] -= 1
                if mp[nums[l]] ==0:
                    del mp[nums[l]]
                l+=1
            result = max(result, r-l+1)
        return result