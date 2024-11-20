class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        heapq.heapify(flowers)
        full_bloom = []
        peopleWithIdx = sorted([(t, i) for i, t in enumerate(people)])
        res = [0] * len(people)
        t, i, j = 0, 0, 0
        for t, i in peopleWithIdx:
            while flowers and flowers[0][0] <= t:
                heapq.heappush(full_bloom, flowers[0][1])
                heapq.heappop(flowers)
            while full_bloom and full_bloom[0] < t:
                heapq.heappop(full_bloom)
            res[i] = len(full_bloom)
        return res