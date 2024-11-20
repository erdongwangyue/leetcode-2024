class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = 0
        visited = set()
        def dfs(r, c, curr):
            nonlocal res
            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visited or grid[r][c] == 0:
                res = max(res, curr)
                return 
            curr += grid[r][c]
            visited.add((r, c))
            for dr, dc in directions:
                newD, newC = r + dr, c + dc
                dfs(newD, newC, curr)
            visited.remove((r, c))
            curr -= grid[r][c]
            return
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0:
                    dfs(r, c, 0)
        return res
