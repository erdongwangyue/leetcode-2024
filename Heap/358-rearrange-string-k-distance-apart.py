class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        res = ""
        counts = collections.Counter(s)
        heap = [(-cnt, c) for c, cnt in counts.items()]
        heapq.heapify(heap)

        q = deque()
        while heap or q:
            if not heap and len(res) < q[0][0]:
                break
            while q and len(res) >= q[0][0]:
                _, c, cnt = q.popleft()
                heapq.heappush(heap, (cnt, c))
            
            cnt, c = heapq.heappop(heap)
            res += c
            if cnt + 1:
                q.append((len(res) + k - 1, c, cnt + 1))
        return res if len(res) == len(s) else ""
