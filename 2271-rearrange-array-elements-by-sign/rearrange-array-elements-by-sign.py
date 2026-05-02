class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pve = 0
        nve = 1
        n = len(nums)
        result = [0] *n
        for i in range(0,n):
            if nums[i]<0:
                result[nve] = nums[i]
                nve+=2
            else:
                result[pve] = nums[i]   
                pve+=2
        return result