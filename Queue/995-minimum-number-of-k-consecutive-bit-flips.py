class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        # q stores index starting at which the following k are flipped
        res = 0
        q = deque()

        for i in range(len(nums)):
            while q and q[0] + k - 1 < i:
                q.popleft()
            # this checks whether a bit is currently a 0
            if (nums[i] + len(q)) % 2 == 0:
                if i + k - 1 < len(nums):
                    q.append(i)
                    res += 1
                else:
                    return -1
        return res
