class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # 1 Edge case
        # 2 Do 2 things to stations
        # 3 Maintain, prevLoc, res, currTank
        # 4 MaxHeap -> -fuel
        if startFuel >= target:
            return 0
        stations.sort()
        stations.append([target, float("inf")])
        maxHeap = []
        prevLocation = 0
        res = 0
        tank = startFuel
        for location, capacity in stations:
            tank -= location - prevLocation
            while maxHeap and tank < 0:
                tank -= heapq.heappop(maxHeap)
                res += 1

            if tank < 0:
                return -1

            heapq.heappush(maxHeap, - capacity)
            prevLocation = location
        return res

