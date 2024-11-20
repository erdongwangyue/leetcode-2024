class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # res
        # visited, set of used (node, edge color that reached it)
        # q, (node, dist, color)
        # after popping do what?

        # visited!!!



        ans = [-1] * n
        visited = set((0, None))
        q = deque([(0, 0, None)])
        blue = defaultdict(list)
        for u, v in blueEdges:
            blue[u].append(v)
        red = defaultdict(list)
        for u, v in redEdges:
            red[u].append(v)


        while q:
            node, steps, color = q.popleft()
            if ans[node] == -1:
                ans[node] = steps
            if color != "R":
                for nei in red[node]:
                    if (nei, "R") not in visited:
                        visited.add((nei, "R"))
                        q.append((nei, steps + 1, "R"))
            if color != "B":
                for nei in blue[node]:
                    if (nei, "B") not in visited:
                        visited.add((nei, "B"))
                        q.append((nei, steps + 1, "B"))


        return ans   