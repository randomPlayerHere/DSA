class Solution:
    def maxDepth(self, s: str) -> int:
        max_val = 0
        count = 0
        for c in s:
            if c == "(":
                count+=1
            elif c==")":
                count -=1
            max_val = max(max_val, count)
        return max_val
        