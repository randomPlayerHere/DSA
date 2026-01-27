class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def tabulation(word, pattern):
            n, m = len(word), len(pattern)
            dp = [[False] * (m + 1) for _ in range(n + 1)]
            dp[0][0] = True
            for j in range(1, m + 1):
                if pattern[j - 1] == '*':
                    dp[0][j] = dp[0][j - 1]
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if pattern[j - 1] == word[i - 1] or pattern[j - 1] == '?':
                        dp[i][j] = dp[i - 1][j - 1]
                    elif pattern[j - 1] == '*':
                        dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            return dp[n][m]
        return tabulation(s,p)