class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # how to write start array?

        start = sorted([interval[0] for interval in intervals])
        end = sorted([interval[1] for interval in intervals])
        res, count = 0, 0
        s, e = 0, 0
        while s < len(start):
            if start[s] < end[e]:
                count += 1
                s += 1
                res = max(res, count)
            else:
                count -= 1
                e += 1
            
        return res