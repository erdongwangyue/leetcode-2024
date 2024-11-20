class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        target = (ROWS - 1, COLS - 1)



        q = deque([(0, 0, k, 0)])
        visited = set([(0, 0, k)])

        while q:
            r, c, k_remain, steps = q.popleft()
            if (r, c) == target:
                return steps
            # if k_remain > 0:
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < ROWS and 0 <= new_c < COLS:
                    # k_remain -= grid[new_r][new_c]
                    if k_remain - grid[new_r][new_c] >= 0 and (new_r, new_c, k_remain - grid[new_r][new_c]) not in visited:
                        visited.add((new_r, new_c, k_remain - grid[new_r][new_c]))
                        q.append((new_r, new_c, k_remain - grid[new_r][new_c], steps + 1))
        return -1










        if k >= ROWS + COLS - 2:
            return ROWS + COLS - 2

        q = deque([(0, (0, 0, k))])
        seen = set([0, 0, k])

        while q:
            
            steps, (r, c, k) = q.popleft()

            if (r, c) == target:
                return steps

            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if (0 <= newR < ROWS) and (0 <= newC < COLS):
                    new_eliminations = k - grid[newR][newC]
                    new_state = (newR, newC, new_eliminations)
                    # add the next move in the queue if it qualifies
                    if new_eliminations >= 0 and new_state not in seen:
                        seen.add(new_state)
                        q.append((steps + 1, new_state))

        # did not reach the target
        return -1