class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(k):
            count = 0
            for i in piles:
                count+= -(-i//k)
            if count <=h:
                return True
            return False
        
        low = 1
        high = max(piles)
        res = 1
        while(low<=high):
            mid = (low+high)//2
            if canEat(mid):
                res = mid
                high = mid-1
            else:
                low = mid+1
        return res
        