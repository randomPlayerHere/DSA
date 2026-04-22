class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        slow = 0
        for fast in range(0,n):
            if nums[fast] !=0:
                nums[slow] = nums[fast]
                slow+=1
        for i in range(slow, n):
            nums[i] = 0
            