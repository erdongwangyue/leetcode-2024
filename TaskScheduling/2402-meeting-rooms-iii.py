class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        res = [0] * n
        used = []
        heapq.heapify(used)
        available = [i for i in range(n)]
        meetings.sort()
        for start, end in meetings:
            while used and used[0][0] <= start:
                time, room = heapq.heappop(used)
                heapq.heappush(available, room)
            if not available:
                end_time, room = heapq.heappop(used)
                end = end_time + (end - start)
                heapq.heappush(available, room)
            room = heapq.heappop(available)
            res[room] += 1
            heapq.heappush(used, (end, room))
        return res.index(max(res))