class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        def mergeSort(inputList):
            if len(inputList) < 2:
                return inputList
            leftArray = mergeSort(inputList[(len(inputList)//2):])
            rightArray = mergeSort(inputList[:(len(inputList)//2)])
            return merge(leftArray, rightArray)

        def merge(leftArray, rightArray):
            leftPointer, rightPointer = 0, 0
            combinedArr = []
            while leftPointer < len(leftArray) and rightPointer < len(rightArray):
                if leftArray[leftPointer] < rightArray[rightPointer]:
                    combinedArr.append(leftArray[leftPointer])
                    leftPointer += 1
                else:
                    combinedArr.append(rightArray[rightPointer])
                    rightPointer += 1
            combinedArr.extend(leftArray[leftPointer:])
            combinedArr.extend(rightArray[rightPointer:])
            return combinedArr
        
        fullList = []
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                fullList.append(matrix[x][y])
        return mergeSort(fullList)[k-1]