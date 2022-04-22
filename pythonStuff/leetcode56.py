class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        if len(intervals) == 1:
            return intervals
        x = 0
        results = []
        while x <= len(intervals)-1:
            if x == len(intervals)-1:
                results.append(intervals[x])
                x+=1
            elif intervals[x][1] >= intervals[x+1][0] and intervals[x][0] <= intervals[x+1][1]:
                if intervals[x+1][0] >= intervals[x][0]:
                    intervals[x+1][0] = intervals[x][0]
                if intervals[x][1] > intervals[x+1][1]:
                    intervals[x+1][1] = intervals[x][1]
                x += 1
            else:
                results.append(intervals[x])
                x += 1
        return results