class Solution:
    def buildMatrix(self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:
        row_graph = defaultdict(list)
        for u,v in rowConditions:
            # below -> above in graph pls
            row_graph[v].append(u)
        
        col_graph = defaultdict(list)
        for u,v in colConditions:
            # left -> right in graph
            col_graph[u].append(v)
        
        def topo(graph):
            indegree = [0] *(k+1)
            topo = []
            for u in range(1, k+1):
                for v in graph[u]:
                    indegree[v] +=1
            z = []
            for i in range(1, k+1):
                if indegree[i] ==0:
                    z.append(i)
            q = deque(z)
            while q:
                node = q.popleft()
                topo.append(node)
                for nei in graph[node]:
                    indegree[nei]-=1
                    if indegree[nei] ==0:
                        q.append(nei)
            return topo
        
        row_topo = topo(row_graph)
        col_topo = topo(col_graph)

        if len(col_topo) !=k or len(row_topo) !=k:
            return []
        
        
        row_topo = row_topo[::-1]


        mat = [[0]*k for _ in range(k)]

        for i in range(k):
            for j in range(k):
                if row_topo[i] == col_topo[j]:
                    mat[i][j] = col_topo[j]
        
        return mat

