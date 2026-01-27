class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1,len2 = len(word1), len(word2)
        # def recur(i,j):
        #     if i<0:
        #         return j+1
        #     if j<0:
        #         return i+1
        #     if word1[i] == word2[j]:
        #         return recur(i-1,j-1)
        #     else:
        #         insert = 1+ recur(i,j-1)
        #         delete = 1 + recur(i-1,j)
        #         replace = 1+recur(i-1,j-1)
        #         return min(insert,delete,replace)
        # return recur(len1-1,len2-1) 

        dp = [[None]*len2 for _ in range(len1)]
        def memo(i,j):
            if i<0:
                return j+1
            if j<0:
                return i+1
            if dp[i][j] is not None:
                return dp[i][j]
            if word1[i] == word2[j]:
                dp[i][j] = memo(i-1,j-1)
            else:
                insert = 1+ memo(i,j-1)
                delete = 1 + memo(i-1,j)
                replace = 1+memo(i-1,j-1)
                dp[i][j] = min(insert, delete, replace)
            return dp[i][j]
        return memo(len1-1, len2-1)

            
            