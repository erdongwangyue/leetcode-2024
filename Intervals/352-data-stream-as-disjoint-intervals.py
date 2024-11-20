class SummaryRanges:

    def __init__(self):
        self.numSet = set()

    def addNum(self, value: int) -> None:
        self.numSet.add(value)

    def getIntervals(self) -> List[List[int]]:
        res = []
        numList = sorted(list(self.numSet))
        for num in numList:
            if res and res[-1][1] + 1 == num:
                res[-1][1] = num
            else:
                res.append([num, num])
        return res


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()