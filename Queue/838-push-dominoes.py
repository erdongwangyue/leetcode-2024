class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        doms = list(dominoes)
        q = deque()

        # Don't forget
        for i, c in enumerate(doms):
            if c != ".":
                q.append((i, c))

        while q:
            i, c = q.popleft()
            if c == "L":
                if i >= 1 and doms[i - 1] == ".":
                    doms[i - 1] = "L"
                    q.append((i - 1, "L"))
            elif c == "R":
                if i + 1 < len(doms) and doms[i + 1] == ".":
                    if i + 2 < len(doms) and doms[i + 2] == "L":
                        q.popleft()
                    else:
                        doms[i + 1] = "R"
                        q.append((i + 1, "R"))
        return "".join(doms)
        