class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) == 1:
            return intervals
        x = 0
        results = []
        while x <= len(intervals)-1:
            if x == len(intervals):
                results.append(intervals[x])
                x+=1
            elif intervals[x][1] >= intervals[x+1][0]:
                intervals[x+1][0] = intervals[x][0]
                x += 1
            else:
                results.append(intervals[x])
                x += 1
        return results

Solution.merge(Solution, [[1,3],[2,6],[8,10],[15,18]])