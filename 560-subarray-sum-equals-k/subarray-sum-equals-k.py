class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mp = dict()
        psum = 0
        result = 0
        mp[0] = 1
        for r in range(n):
            psum +=nums[r]
            needed = psum-k
            if mp.get(needed, -1) !=-1:
                result += mp[needed]
            mp[psum] = mp.get(psum, 0) +1
        return result


            