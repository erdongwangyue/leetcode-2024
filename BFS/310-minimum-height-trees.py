class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # edge_cnt node -> number of edges,init to empty
        # q - leaves
        # exit condition: n <= 2
        # after popping, decrement n, for nei, deverment count and check whether to append in leaves
        if n == 1:
            return [0]
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        edge_count = {}
        q = deque()
        for node in adj:
            edge_count[node] = len(adj[node])
            if len(adj[node]) == 1:
                q.append(node)

        while q:
            if n <= 2:
                return list(q)
            for _ in range(len(q)):
                node = q.popleft()
                n -= 1
                edge_count[node] -= 1
                for nei in adj[node]:
                    edge_count[nei] -= 1
                    if edge_count[nei] == 1:
                        q.append(nei)
        
        
        
        
        
        
      