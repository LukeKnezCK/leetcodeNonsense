class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        def mergeSort(nums):
            if len(nums) < 2:
                return nums
            leftArray = mergeSort(nums[0:len(nums)//2])
            rightArray = mergeSort(nums[len(nums)//2:])
            result = []
            leftPointer, rightPointer= 0, 0
            while leftPointer < len(leftArray) and rightPointer < len(rightArray):
                if leftArray[leftPointer] <= rightArray[rightPointer]:
                    result.append(leftArray[leftPointer])
                    leftPointer += 1
                else:
                    result.append(rightArray[rightPointer])
                    rightPointer += 1
            result.extend(leftArray[leftPointer:])
            result.extend(rightArray[rightPointer:])
            return result
    
        sortedNums = mergeSort(nums)
        
        counter = 0
        for x in sortedNums:
            if not x == counter:
                return counter
            counter += 1
        return counter