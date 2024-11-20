class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # no visited set, use island_id to mark grid as visited
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        island_areas = {}
        island_id = -1

        def dfs(r, c):
            if r >= 0 and r < ROWS and c >= 0 and c < COLS and grid[r][c] == 1:
                area = 1
                grid[r][c] = island_id
                for dr, dc in directions:
                    newR, newC = r + dr, c + dc
                    area += dfs(newR, newC)
                return area
            return 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    island_areas[island_id] = area
                    # Don't forget
                    island_id -= 1

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    area = 1
                    surroundings = set()
                    for dr, dc in directions:
                        newR, newC = r + dr, c + dc
                        if 0 <= newR < ROWS and 0 <= newC < COLS and grid[newR][newC] != 0:
                            surroundings.add(grid[newR][newC])
                    for island_id in surroundings:
                        area += island_areas[island_id]
                    res = max(res, area)
        return res if res else ROWS * COLS
