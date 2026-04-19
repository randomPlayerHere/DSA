class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total_count = 0
        hm = {0:1}
        n = len(nums)
        ps = 0
        for i in range(n):
            ps +=nums[i]
            wanted = ps-k
            count = hm.get(wanted,0)
            total_count+=count
            hm[ps] = hm.get(ps,0)+1
        return total_count