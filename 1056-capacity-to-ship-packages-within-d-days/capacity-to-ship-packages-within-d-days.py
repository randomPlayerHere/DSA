class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isValid(w):
            weight = 0
            day = 1
            for i in range(len(weights)):
                if weight + weights[i] <= w:
                    weight += weights[i]
                else:
                    day +=1
                    weight = weights[i]
            return day <=days
        low,high = max(weights),sum(weights)
        result = float('inf')
        while low<=high:
            mid = (low+high)//2
            if isValid(mid):
                result = min(result, mid)
                high = mid-1
            else:
                low = mid+1
        return result
