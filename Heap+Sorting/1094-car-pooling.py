class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        toPickup, toDropoff = [[f, t, n] for n, f, t in trips], [] # minHeaps
        heapq.heapify(toPickup)

        while toPickup:
            p, d, n = heapq.heappop(toPickup)
            while toDropoff and toDropoff[0][0] <= p:
                _, nToDropoff = heapq.heappop(toDropoff)
                capacity += nToDropoff
            if capacity < n:
                return False
            capacity -= n
            heapq.heappush(toDropoff, [d, n])
        return True