# Initial brute force approach
# def maxArea(self, height: List[int]) -> int:
#         currentArea = 0
#         highScore = 0
#         for x in range(len(height)):
#             for y in range(len(height)):
#                 if y == x:
#                     currentArea = 0
#                 else:
#                     if height[x] > height[y]:
#                         length = abs(x-y)
#                         currentArea = length*height[y]
#                     else:
#                         length = abs(x-y)
#                         currentArea = length*height[x]
#                 if currentArea > highScore:
#                     highScore = currentArea
#         return highScore

# Improved approach
def maxArea(self, height: List[int]) -> int:
        highScore = 0
        x, y = 0, len(height)-1
        while x < y:
            if height[x] > height[y]:
                currentScore = height[y]*(y-x)
                if currentScore > highScore:
                    highScore = currentScore
                y -= 1
            else:
                currentScore = height[x]*(y-x)
                if currentScore > highScore:
                    highScore = currentScore
                x += 1
        return highScore