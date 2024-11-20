class Solution:
    def findMin(self, nums: List[int]) -> int:
        # What to do when num[l] == num[m]? search the right because in this case l == m

        left, right = 0, len(nums) - 1
        res = nums[0]
        while left <= right:
            if nums[left] < nums[right]:
                return min(res, nums[left])
            mid = (left + right) // 2
            res = min(res, nums[mid])
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return res
