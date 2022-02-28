from sqlite3 import Row


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        updateCords = {}
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if matrix[x][y] == 0:
                    updateCords[f'{x}{y}'] = [x,y]
        for z in updateCords.values():
            row = z[0]
            column = z[1]
            for x in range(len(matrix[0])):
                matrix[row][x] = 0
            for y in range(len(matrix)):
                matrix[y][column] = 0

Solution.setZeroes(Solution, [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]])