class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t = {}
        t_s = {}
        for a,b in zip(s,t):
            if s_t.get(a,b) !=b:
                return False
            if t_s.get(b,a) !=a:
                return False
            s_t[a] = b
            t_s[b] = a
        return True

