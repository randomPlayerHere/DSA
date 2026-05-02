class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def swap(i,j):
            nums[i], nums[j] = nums[j], nums[i]

        n = len(nums)
        if n<2:
            return
        bp = -1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                bp = i
                break
        if bp ==-1:
            nums.sort()
            return
        low, low_dif = -1, float('inf')
        for i in range(n-1, i, -1):
            if nums[i] > nums[bp]:
                swap(i,bp)
                break
        nums[bp+1:] = sorted(nums[bp+1:])

        
        
