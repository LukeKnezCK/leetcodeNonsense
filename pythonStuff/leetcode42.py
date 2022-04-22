def trap(height: list[int]) -> int:
        leftWallPosition = 0
        leftWall = height[0]
        counter = 0
        totalWater = 0
        position = 1
        while position < len(height):
            if position == len(height)-1 and height[position] < leftWall:
                if height[position] <= leftWall - 1:
                    heightHolder= []
                    position = leftWallPosition+1
                    for x in range(position, len(height)):
                        heightHolder.append(height[x])
                    leftWall = max(heightHolder)
                    counter = 0
                else:
                    leftWall = height[leftWallPosition+1]
                    leftWallPosition += 1
                    position = leftWallPosition + 1
                    counter = 0
                
            elif height[position] >= leftWall:
                totalWater += counter
                counter = 0
                leftWall = height[position]
                leftWallPosition = position
                position += 1
            else:
                counter += (leftWall - height[position])
                position += 1
        return totalWater
