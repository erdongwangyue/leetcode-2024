class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
        
        def dfs(src):
            if src in visiting:
                return float("inf")
            if src in visited:
                return 0
            colorIndex = ord(colors[src]) - ord('a')
            count[src][colorIndex] = 1
            visiting.add(src)
            for nei in adj[src]:
                if dfs(nei) == float("inf"):
                    return float("inf")
                for c in range(26):
                    count[src][c] = max(
                        count[src][c],
                        (1 if c == colorIndex else 0) + count[nei][c]
                    )
            visiting.remove(src)
            visited.add(src)
            return max(count[src])

        n, res = len(colors), 0
        visited, visiting = set(), set()
        count = [[0] * 26 for _ in range(n)] # count[node][color] -> max freq color starting at node
        for i in range(n):
            res = max(res, dfs(i))

        return res if res != float("inf") else -1