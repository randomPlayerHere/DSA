from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        result = []
        n,m = len(mat), len(mat[0])
        for i in range(0,n):
            for j in range(0,m):
                mp[i+j].append(mat[i][j])
        for key in sorted(mp.keys()):
            value = mp[key]
            if key%2==0:
                result.extend(value[::-1])
            else:
                result.extend(value)
        return result
        