class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        ROWS, COLS = m, n
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        dp = {}
        MOD = 10 ** 9 + 7
        def dfs(r, c, moves):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 1
            if moves == 0:
                return 0
            if (r, c, moves) in dp:
                return dp[(r, c, moves)]
            res = 0
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                res += dfs(newR, newC, moves - 1)
            res %= MOD
            dp[(r, c, moves)] = res
            return res
        return dfs(startRow, startColumn, maxMove)

