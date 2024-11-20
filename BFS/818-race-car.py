class Solution:
    def racecar(self, target: int) -> int:

        # what to put in queue? moves, pos, speed
        # keep visited? what to put in it? (pos, speed)
        # when to check in visited and add to visited? After pop, not in nei's logic
        # what is the condition of R? what to do in it?

        q = deque([(0, 0, 1)]) # move, pos, speed
        visited = set()

        while q:
            moves, pos, speed = q.popleft()
            if pos == target:
                return moves
            if (pos, speed) in visited:
                continue
            visited.add((pos, speed))
            q.append((moves + 1, pos + speed, speed * 2))
            if (pos + speed > target and speed > 0) or (pos + speed < target and speed < 0):
                speed = -1 if speed > 0 else 1
                q.append((moves + 1, pos, speed))

            
