class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        initialList = [1,1]
        fullSet = [[1], [1,1]]
        if numRows == 1:
            return fullSet[:1]
        elif numRows == 2:
            return fullSet
        for x in range(numRows-2):
            addingList = [1]
            rightPointer = 1
            leftPointer = 0
            while rightPointer < len(initialList):
                addingList.append(initialList[leftPointer]+initialList[rightPointer])
                rightPointer += 1
                leftPointer += 1
            addingList.append(1)
            fullSet.append(addingList)
            initialList = addingList
        return fullSet