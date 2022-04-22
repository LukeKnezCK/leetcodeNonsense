#This is a horrible solution lolol
#Should modularize most of these lines into functions for easier readability
#But Im not going to put in that much work for a leetcode question 

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        if len(matrix) == 1:
            return matrix[0]
        
        while len(matrix) > 0:
            for x in matrix[0]:
                result.append(x)
            matrix.pop(0)
            if len(matrix) == 0:
                return result
            
            for x in matrix:
                result.append(x.pop())
            z = len(matrix)-1
            while z >= 0:
                if len(matrix[z]) == 0:
                    matrix.pop()
                z -= 1
            if len(matrix) == 0:
                return result
            
            y = len(matrix[0])-1
            while y >= 0:
                result.append(matrix[len(matrix)-1].pop())
                y -= 1
            matrix.pop()
            
            if len(matrix) == 0:
                return result
            z = len(matrix)-1
            while z >= 0:
                if len(matrix[z]) == 0:
                    matrix.pop()
                z-= 1
            if len(matrix) == 0:
                return result

            y = len(matrix)-1
            while y >= 0:
                result.append(matrix[y].pop(0))
                y -= 1
            z = len(matrix)-1
            while z >= 0:
                if len(matrix[z]) == 0:
                    matrix.pop()
                z-= 1
            if len(matrix) == 0:
                return result
        return result

Solution.spiralOrder(Solution, [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]])