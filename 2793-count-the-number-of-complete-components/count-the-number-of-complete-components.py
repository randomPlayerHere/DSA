from collections import deque, defaultdict
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def edges_to_adj_list(n, edges):
            graph = defaultdict(list)
            for n1, n2 in edges:
                graph[n1].append(n2)
                graph[n2].append(n1)
            return graph
    
        graph = edges_to_adj_list(n, edges)
        visited = [0] *n
        count = 0

        def bfs(root):
            que = deque([root])
            visited[root] = 1
            subgroup = set()
            while que:
                node = que.popleft()
                subgroup.add(node)
                for nei in graph[node]:
                    if visited[nei] ==0:
                        visited[nei] = 1
                        que.append(nei)
            for node in subgroup:
                if subgroup - {node} == set(graph[node]):
                    continue
                else:
                    return False
            return True
        
        for node in range(n):
            if visited[node] ==0:
                if bfs(node):
                    count+=1
            else:
                continue
        return count





