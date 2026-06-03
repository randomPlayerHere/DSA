class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for i in range(len(min(strs, key=len))):
            char = strs[0][i]
            for word in strs:
                if word[i] !=char:
                    return result
            result = result + char
        return result