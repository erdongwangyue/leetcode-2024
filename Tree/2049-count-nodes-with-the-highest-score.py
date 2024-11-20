class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        sizes = {}
        adj = defaultdict(list)
        for i, p in enumerate(parents):
            adj[p].append(i)

        def dfs(i):
            if i in sizes:
                return sizes[i]
            size = 1
            for child in adj[i]:
                size += dfs(child)
            sizes[i] = size
            return size

        dfs(0)

        res, count = 0, 0
        for i in range(n):
            score = 1
            for child in adj[i]:
                score *= sizes[child]
            if i != 0:
                score *= n - sizes[i]
            if res < score:
                res = score
                count = 1
            elif res == score:
                count += 1
        return count