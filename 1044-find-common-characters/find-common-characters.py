from collections import defaultdict
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = Counter(words[0])
        for w in words:
            cur_cnt = Counter(w)
            for c in cnt:
                cnt[c] = min(cur_cnt[c], cnt[c])
        res = []
        for c in cnt:
            for _ in range(cnt[c]):
                res.append(c)
        return res