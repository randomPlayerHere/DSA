class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count,elem = 0, nums[0]
        for i in range(n):
            if nums[i]==elem:
                count+=1
            else:
                count -=1
                if count <0:
                    elem = nums[i]
                    count=0
        return elem