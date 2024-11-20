class Solution:
    def findKthLargest(self, nums, k):
        def dfs(nums, k):
            mid, left, right = [], [], []
            pivot = random.choice(nums)

            for num in nums:
                if num < pivot:
                    right.append(num)
                elif num > pivot:
                    left.append(num)
                else:
                    mid.append(num)

            if k > len(left) and k <= len(left) + len(mid):
                return pivot
            elif k > len(left) + len(mid):
                return dfs(right, k - len(left) - len(mid))
            else:
                return dfs(left, k)
        return dfs(nums, k)
            
            