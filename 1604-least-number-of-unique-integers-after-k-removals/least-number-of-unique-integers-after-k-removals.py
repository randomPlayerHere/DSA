class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        mp = Counter(arr)
        pairs = sorted(mp.items(), key=lambda x:x[1],reverse=True)
        while k:
            if pairs[-1][1] >k:
                break
            k-= pairs[-1][1]
            del(pairs[-1])
        return len(pairs)
