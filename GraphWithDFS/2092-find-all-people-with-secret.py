class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # secrets: people who have known by far
        # visited: people gets to know at time t
        # time_map: t -> src to dst on passing the secret, and its 2-way
        # input and base case for dfs()?
        # invocation on dfs: for what, for what and if what?

        secrets = set([0, firstPerson])
        time_map = {}
        for s, d, t in meetings:
            if t not in time_map:
                time_map[t] = defaultdict(list)
            time_map[t][s].append(d)
            time_map[t][d].append(s)
        def dfs(src, t):
            if src in visited:
                return
            visited.add(src)
            secrets.add(src)
            for nei in time_map[t][src]:
                dfs(nei, t)

        for t in sorted(time_map.keys()):
            visited = set()
            for src in time_map[t]:
                if src in secrets:
                    dfs(src, t)
        return list(secrets)

      