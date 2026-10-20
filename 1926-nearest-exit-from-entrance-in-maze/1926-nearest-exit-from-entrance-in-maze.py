class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        maxi,maxj = len(maze), len(maze[0])

        def isexit(i,j):
            if (i in (0, maxi-1) or j in (0,maxj-1)) and maze[i][j] == "." and  [i,j] != entrance:
                return True
            return False
        
        delta = [(1,0),(0,1),(-1,0),(0,-1)]
        visited= set()
        q = deque([(entrance[0],entrance[1],0)])
        visited.add((entrance[0], entrance[1]))
        while q:
            i,j,dist = q.popleft()
            if isexit(i,j):
                return dist
            new_dist = dist+1
            for di,dj in delta:
                ni,nj = i+di, j+dj
                if 0<=ni<maxi and 0<=nj<maxj and maze[ni][nj]=="." and (ni,nj) not in visited:
                    visited.add((ni,nj))
                    q.append((ni,nj,new_dist))
        
        return -1


