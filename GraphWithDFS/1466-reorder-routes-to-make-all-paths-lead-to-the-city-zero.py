class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # visited, edges, adj: visited nodes, set of existing edges, adj as if edges were non-directed
        # dfs(target) logic
        visited = set([0])
        edges = {(s, t) for s, t in connections}
        adj = defaultdict(list)

        for s, t in connections:
            adj[s].append(t)
            adj[t].append(s)
        
        res = 0

        def dfs(target):
            nonlocal res
            for nei in adj[target]:
                if nei in visited:
                    continue
                if (nei, target) not in edges:
                    res += 1
                visited.add(nei)
                dfs(nei)
        dfs(0)
        return res
        