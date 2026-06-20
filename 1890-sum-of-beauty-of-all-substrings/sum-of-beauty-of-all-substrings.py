class Solution:
    def beautySum(self, s: str) -> int:
        result = 0
        for a in range(0, len(s)):
            ocur = [0] *26
            for b in range(a, len(s)):
                ocur[ord(s[b]) - ord('a')] +=1
                maxi = 0
                mini = float('inf')
                for i in range(26):
                    maxi = max(ocur[i], maxi)
                    if ocur[i] >=1:
                        mini = min(ocur[i],mini)
                result += maxi-mini
        return result

