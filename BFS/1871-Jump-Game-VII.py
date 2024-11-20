class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # q - idx to be considered
        # farthest - can be reached before curr, init 0
        # start = max(i + minJump, farthest + 1)
        # end = min(len(s), i + maxJump + 1)
        # farthest = i + maxJump
        q, prev_r = deque([0]), 0

        while q:
            curr = q.popleft()
            if curr == len(s) - 1:
                return True
            start, end =  max(curr + minJump, prev_r + 1), min(len(s), curr + maxJump + 1)
            for i in range(start, end):
                if s[i] == "0":
                    q.append(i)

            prev_r = curr + maxJump
        return False


