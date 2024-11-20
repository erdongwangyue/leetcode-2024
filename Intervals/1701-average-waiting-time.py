class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        if not customers or len(customers) == 0:
            return 0

        awaitTime = customers[0][1]
        currEnd = customers[0][1] + customers[0][0]
        for i in range(1, len(customers)):
            arrival, prepareTime = customers[i][0], customers[i][1]
            awaitTime += currEnd - arrival if currEnd > arrival else 0
            awaitTime += prepareTime
            currStart = max(currEnd, arrival)
            currEnd = currStart + prepareTime
        return awaitTime / len(customers)