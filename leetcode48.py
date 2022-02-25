class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        tempList = []
        for l in range(len(matrix)):
            tempList.append([])
        for x in matrix:
            y = 0
            for z in x:
                tempList[y].insert(0,z)
                y+=1
                
                
        matrix.clear()
        for k in tempList:
            matrix.append(k)
                