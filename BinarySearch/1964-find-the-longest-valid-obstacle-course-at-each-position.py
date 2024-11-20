class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        # last_occ = {obstacles[0]: 0}
        # dp = [1] * len(obstacles)
        # for i in range(1, len(obstacles)):
        #     curr = obstacles[i]
        #     for hei in last_occ:
        #         if hei <= curr:
        #             dp[i] = max(dp[i], 1 + dp[last_occ[hei]])
        #     last_occ[curr] = i
        # return dp

        res = []
        dp = [10 ** 8] * (len(obstacles) + 1)
        for n in obstacles:
            idx = bisect.bisect(dp, n)
            res.append(idx + 1)
            dp[idx] = n
        return res