class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQ = collections.deque()
        maxQ = collections.deque()

        l = 0
        res = 0
        for r in range(len(nums)):
            while maxQ and maxQ[-1] < nums[r]:
                maxQ.pop()
            maxQ.append(nums[r])
            while minQ and minQ[-1] > nums[r]:
                minQ.pop()
            minQ.append(nums[r])
            while abs(maxQ[0] - minQ[0]) > limit:
                if nums[l] == maxQ[0]:
                    maxQ.popleft()
                if nums[l] == minQ[0]:
                    minQ.popleft()
                l += 1

            res = max(res, r - l + 1)
        return res