class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = ["".join(sorted(word)) for word in strs]
        mp = defaultdict(list)
        for i in range(len(sorted_strs)):
            mp[sorted_strs[i]].append(strs[i])
        result = [val for _,val in mp.items()]
        return result

            

