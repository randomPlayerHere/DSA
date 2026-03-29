from collections import defaultdict

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        mp = defaultdict(list)
        n,m = len(mat), len(mat[0])
        for i in range(0,n):
            for j in range(0,m):
                mp[i-j].append(mat[i][j])
        for key in mp:
            mp[key].sort(reverse=True)
        for i in range(0,n):
            for j in range(0,m):
                mat[i][j] = mp[i-j].pop()
        return mat
         

