class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        heights.append(0)
        stack = [-1]
        maxRect = 0
        for x in range(len(heights)):
            while heights[x] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = x - stack[-1] - 1
                maxRect = max(maxRect, h * w)
            stack.append(x)
        heights.pop()
        return maxRect

Solution.largestRectangleArea(Solution, [2,1,5,6,2,3])