class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        primit = []
        prev_cut = 0
        count = 0
        for i in range(len(s)):
            count+= 1 if s[i]=="(" else -1
            if count==0:
                primit.append(s[prev_cut+1:i+1-1])
                prev_cut = i+1
        # primit = [s[1:-1] for s in primit]
        return "".join(primit)
        