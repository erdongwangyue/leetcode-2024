class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [[nums1[i], nums2[i]] for i in range(len(nums1))]
        pairs = sorted(pairs, key = lambda p: p[1], reverse = True)
        heap = []
        total = 0
        res = 0
        for n1, n2 in pairs:
            heapq.heappush(heap, n1)
            total += n1
            if len(heap) > k:
                total -= heapq.heappop(heap)
            if len(heap) == k:
                res = max(res, total * n2)
        return res
