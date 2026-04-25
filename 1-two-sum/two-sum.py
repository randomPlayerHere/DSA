class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hash_map = dict()
        for i in range(n):
            needed = target-nums[i]
            if hash_map.get(needed,-1) != -1:
                return [hash_map[needed],i]
            else:
                hash_map[nums[i]] = i
        return []
        
            
