class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def isValid(d):
            count = 0
            bq = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= d:
                    count+=1
                else:
                    bq += count//k
                    count = 0
            bq +=count//k
            if bq >= m:
                return True
            return False
        if (m*k) >len(bloomDay):
            return -1
        low, high = min(bloomDay), max(bloomDay)
        result = float('inf') 
        while low<=high:
            mid = (low+high)//2
            if isValid(mid):
                result = min(mid,result)
                high = mid-1
            else:
                low = mid+1
        return result
            


