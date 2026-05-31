class Solution:
    def frequencySort(self, s: str) -> str:
        mp = Counter(s)
        pairs_sorted = sorted(mp.items(), key=lambda x:x[1], reverse=True)
        result = [c*freq for c,freq in pairs_sorted]
        return "".join(result)