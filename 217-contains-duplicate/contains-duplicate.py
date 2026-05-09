from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mp = Counter(nums)
        for key,val in mp.items():
            if val>1:
                return True
        return False