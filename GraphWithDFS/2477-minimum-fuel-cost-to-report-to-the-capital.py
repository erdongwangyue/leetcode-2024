class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj = defaultdict(list)
        for s, t in roads:
            adj[s].append(t)
            adj[t].append(s)

        res = 0
        def dfs(curr, prev):
            nonlocal res
            passengers = 0
            for nei in adj[curr]:
                if nei != prev:
                    p = dfs(nei, curr)
                    res += int(ceil(p / seats))
                    passengers += p
            # don't forget + 1
            return passengers + 1
        dfs(0, -1)
        return res

