class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        minHeap, currMax = [], 0
        for n in nums:
            origin = n
            while n % 2 == 0:
                n = n // 2
            # what to append for the 1st round?
            minHeap.append((n, max(origin, 2 * n)))
            currMax = max(currMax, n)
        heapq.heapify(minHeap)
        res = float("inf")
        while len(minHeap) == len(nums):
            n, origin = heapq.heappop(minHeap)
            res = min(res, currMax - n)

            if n < origin:
                heapq.heappush(minHeap, (n * 2, origin))
                currMax = max(currMax, n * 2)
        return res