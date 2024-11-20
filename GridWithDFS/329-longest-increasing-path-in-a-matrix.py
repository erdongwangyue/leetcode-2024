class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        dp = {}

        @cache
        def dfs(r, c, prev):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or matrix[r][c] <= prev:
                return 0
            # if (r, c, prev) in dp:
            #     return dp[(r, c, prev)]
            res = 1
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                res = max(res, 1 + dfs(newR, newC, matrix[r][c]))
            # dp[(r, c, prev)] = res
            return res

        res = -1
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c, -1))
        return res