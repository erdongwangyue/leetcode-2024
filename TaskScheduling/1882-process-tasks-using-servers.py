class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)
        unavailable = []
        ans = [0] * len(tasks)
        currTime = 0
        for i in range(len(tasks)):
            currTime = max(currTime, i)
            if len(available) == 0:
                currTime = unavailable[0][0]
            while unavailable and currTime >= unavailable[0][0]:
                t, w, j = heapq.heappop(unavailable)
                heapq.heappush(available, (w, j))
            w, j = heapq.heappop(available)
            ans[i] = j
            heapq.heappush(unavailable, [currTime + tasks[i], w, j])
    
        return ans
            
