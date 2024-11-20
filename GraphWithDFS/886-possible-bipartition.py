class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        colors = [-1] * (n + 1)
        adj = defaultdict(list)
        for a, b in dislikes:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node, color):
            colors[node] = color
            for nei in adj[node]:
                # Review
                if colors[nei] == colors[node]:
                    return False
                if colors[nei] == -1:
                    if not dfs(nei, 1 - color):
                        return False
            return True
        
        for i in range(1, n + 1):
            # Forgotten
            if colors[i] == -1:
                if not dfs(i, 0):
                    return False
        return True

