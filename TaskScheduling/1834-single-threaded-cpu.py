class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        time = 0
        remaining_tasks = [(e, p, i) for i, [e, p] in enumerate(tasks)]
        heapq.heapify(remaining_tasks)

        enqueued_tasks = []
        while remaining_tasks or enqueued_tasks:
            if not enqueued_tasks and remaining_tasks[0][0] > time:
                time = remaining_tasks[0][0]
            while remaining_tasks and remaining_tasks[0][0] <= time:
                _, p, i = heapq.heappop(remaining_tasks)
                heapq.heappush(enqueued_tasks, (p, i))
            p, i = heapq.heappop(enqueued_tasks)
            res.append(i)
            time += p
        return res