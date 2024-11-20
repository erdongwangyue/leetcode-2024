class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # stack -> (currNum, min among everything before curr num)
        currMin = nums[0]
        stack = [(nums[0], currMin)]

        for n in nums[1:]:
            while stack and stack[-1][0] <= n:
                stack.pop()
            if stack and stack[-1][1] < n:
                return True
            stack.append((n, currMin))
            currMin = min(n, currMin)
        return False
