class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # order of maintaining: first pop left from q, then adjust l
        
        q = deque()
        res = []
        l, r = 0, 0
        for r in range(len(nums)):
            while q and q[-1][1] < nums[r]:
            # while q and q[-1] < nums[r]:
                q.pop()
            q.append((r, nums[r]))

            if r >= k - 1:
                if l > q[0][0]:
                    q.popleft()
                res.append(q[0][1])
                l += 1
        return res