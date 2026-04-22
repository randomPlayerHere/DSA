class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n==1:
            return True
        count = 1
        for i in range(1,2*n):
            i = i%n
            if nums[i] >= nums[i-1]:
                count +=1
            else:
                count = 1
            if count ==n:
                return True
        return False