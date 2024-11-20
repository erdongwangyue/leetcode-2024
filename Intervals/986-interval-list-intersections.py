class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        pointer1, pointer2 = 0, 0
        res = []
        while pointer1 < len(firstList) and pointer2 < len(secondList):
            low = max(firstList[pointer1][0], secondList[pointer2][0])
            high = min(firstList[pointer1][1], secondList[pointer2][1])
            if low <= high:
                res.append([low, high])
            if firstList[pointer1][1] < secondList[pointer2][1]:
                pointer1 += 1
            else:
                pointer2 += 1
        return res