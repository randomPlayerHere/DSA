from collections import defaultdict, deque
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        visited = set()
        restricted = set(restricted)
        def edges_to_adj_list(n, edges):
            graph = defaultdict(list)
            for n1, n2 in edges:
                graph[n1].append(n2)
                graph[n2].append(n1)
            return graph
        graph = edges_to_adj_list(n, edges)
            
        def dfs(node):
            if node in restricted:
                return
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        
        def bfs(root):
            que = deque([root])
            visited.add(root)
            while que:
                node = que.popleft()
                for nei in graph[node]:
                    if nei in restricted:
                        continue
                    elif nei not in visited:
                        visited.add(nei)
                        que.append(nei)
        
        dfs(0)
        return len(visited)

