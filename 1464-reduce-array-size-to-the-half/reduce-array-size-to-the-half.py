class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        mp = Counter(arr)
        freq = len(arr)
        pairs = sorted(mp.items(), key= lambda x:x[1])
        count = 0
        while freq > len(arr)//2:
            count+=1
            freq -= pairs[-1][1]
            del(pairs[-1])
        return count