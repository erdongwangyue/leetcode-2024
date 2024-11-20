from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_list = SortedList([])
        res = []
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            idx = sorted_list.bisect_left(num)
            res.append(idx)
            sorted_list.add(num)
        return res[::-1]
        
        
        sorted_list = SortedList([])
        res = []

        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]

            idx = sorted_list.bisect_left(num)
            res.append(idx)
            sorted_list.add(num)
        return res[::-1]