# Time: O(n) Space: O(1)

class Solution(object):
    def gridGame(self, grid):
        # how to explain https://www.youtube.com/watch?v=N4wDSOw65hI&t=570s starting 8th minutes
        res = float("inf")
        left = 0
        right = sum(grid[0])


        for a, b in zip(grid[0], grid[1]):
            right -= a
            res = min(res, max(left, right))
            left += b
        return res