class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        maxCount = 1
        for point in range(len(points)):
            for pointTwo in range(point+1,len(points)):
                xChange = points[point][0]-points[pointTwo][0]
                yChange = points[point][1]-points[pointTwo][1]
                try:
                    slope = xChange/yChange
                except ZeroDivisionError:
                    slope = "Zero"
                curCount = self.helperPoints(points[point], slope, points[pointTwo+1:]) + 2
                if curCount > maxCount:
                    maxCount = curCount
        return maxCount
            
    def helperPoints(self,anchor, slope, points):
        if len(points) < 1:
            return 0
        else:
            xChange = anchor[0] - points[0][0]
            yChange = anchor[1] - points[0][1]
            try:
                checkSlope = xChange/yChange
            except ZeroDivisionError:
                checkSlope = "Zero"
            if checkSlope == slope:
                return self.helperPoints(anchor, slope, points[1:]) + 1
            else:
                return self.helperPoints(anchor, slope, points[1:])
