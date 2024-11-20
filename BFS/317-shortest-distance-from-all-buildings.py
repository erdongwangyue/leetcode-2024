class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # BFS from buildings, not empty land
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        distances = [[0] * COLS for _ in range(ROWS)]

        EMPTY_LAND = 0
        BUILDING = 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    q = deque([(r, c, 0)])
                    while q:
                        currR, currC, dist = q.popleft()
                        for dr, dc in directions:
                            newR, newC = currR + dr, currC + dc
                            if 0 <= newR < ROWS and 0 <= newC < COLS and grid[newR][newC] == EMPTY_LAND:
                                q.append((newR, newC, dist + 1))
                                distances[newR][newC] += dist + 1
                                grid[newR][newC] -= 1
                    EMPTY_LAND -= 1

        res = float("inf")
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == EMPTY_LAND:
                    res = min(res, distances[r][c])
        return res if res != float("inf") else -1
