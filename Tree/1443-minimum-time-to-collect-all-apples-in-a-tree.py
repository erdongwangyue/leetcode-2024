class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # Note: this is a non-binary tree
        # input to dfs()? i, parent. Output？ number of steps
        # base case? if len(i) == 1 (when it is a leaf), return 2 if what else 0
        
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        def dfs(i, prev):
            if len(adj[i]) == 1:
                return 2 if hasApple[i] else 0
            res = 0
            for nei in adj[i]:
                if nei != prev:
                    new = dfs(nei, i)
                    res += new + 2 if new > 0 else 0
            return res

        return dfs(0, -1)