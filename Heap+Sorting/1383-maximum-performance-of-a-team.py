class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        choices = sorted(zip(efficiency, speed), reverse=True)
        minHeap = []
        MOD = 10 ** 9 + 7
        res = 0
        total = 0
        for i in range(len(choices)):
            efficiency, speed = choices[i]
            total += speed
            if i >= k:
                minSpeed = heapq.heappop(minHeap)
                total -= minSpeed
            res = max(res, (total * efficiency))
            heapq.heappush(minHeap, speed)
        return res % MOD
            