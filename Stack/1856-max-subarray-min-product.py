class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        # res - int
        # stack - (n, idx of the starting point of subarray where n is the min)
        # prefix - length of n + 1 prefix.append(prefix[-1] + )
        res = 0
        stack = []
        prefix = [0]
        for n in nums:
            prefix.append(prefix[-1] + n)

        for i, n in enumerate(nums):
            newStart = i
            while stack and stack[-1][-1] > n:
                start, val = stack.pop()
                total = prefix[i] - prefix[start]
                res = max(res, val * total)
                newStart = start
            stack.append((newStart, n))

        for start, val in stack:
            total = prefix[len(nums)] - prefix[start]
            res = max(res, val * total)
        return res % (10**9 + 7)