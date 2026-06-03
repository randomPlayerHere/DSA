import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(k):
            hrs= sum([math.ceil(i/k) for i in piles])
            if hrs <=h:
                return True
            else:
                False
        low ,high = 1, max(piles)
        ans = max(piles)
        while low<=high:
            mid = (low+high)//2
            if canEat(mid):
                high = mid-1
                ans = mid
            else:
                low = mid+1
        return ans

