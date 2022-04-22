class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lowerBound = 0
        h = len(matrix)
        w = len(matrix[0])
        
        def columnFind(x, lowerBound, matrix):
            for y in range(x,h):
                if matrix[y][lowerBound] == target:
                    return True
            return False
        
        def rowFind(x, lowerBound, matrix):
            for y in range(lowerBound,w):
                if matrix[x][y] == target:
                    return True
            return False
            
        for x in range(h):    
            if matrix[x][lowerBound] <= target <= matrix[x][w-1]:
                if rowFind(x, lowerBound, matrix):
                    return True
            if matrix[x][lowerBound] <= target <= matrix[h-1][lowerBound]:
                if columnFind(x, lowerBound, matrix):
                    return True
            lowerBound += 1
            if lowerBound >= h or lowerBound >= w:
                return False
        return False