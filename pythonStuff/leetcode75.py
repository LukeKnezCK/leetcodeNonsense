class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for x in range(len(nums)):
            for y in range(x, len(nums)):
                if nums[y] < nums[x]:
                    nums[x], nums[y] = nums[y], nums[x]
                    
        return nums

# A mergesort solution i dabbled with before i decided to just use bubble sort
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        else:
            midPoint = len(nums)//2
            leftArray = self.sortHelper(nums[:midPoint])
            rightArray = self.sortHelper(nums[midPoint:])
            leftPointer,rightPointer = 0,0
            nums.clear()
            while leftPointer <= len(leftArray)-1 and rightPointer <= len(rightArray)-1:
                if leftArray[leftPointer] <= rightArray[rightPointer]:
                    nums.append(leftArray[leftPointer])
                    leftPointer += 1
                else:
                    nums.append(rightArray[rightPointer])
                    rightPointer += 1
            nums.extend(leftArray[leftPointer:])
            nums.extend(rightArray[rightPointer:])
        
    def sortHelper(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        else:
            midPoint = len(nums)//2
            leftArray = self.sortHelper(nums[:midPoint])
            rightArray = self.sortHelper(nums[midPoint:])
            leftPointer,rightPointer = 0,0
            resultArray = []
            while leftPointer <= len(leftArray)-1 and rightPointer <= len(rightArray)-1:
                if leftArray[leftPointer] <= rightArray[rightPointer]:
                    resultArray.append(leftArray[leftPointer])
                    leftPointer += 1
                else:
                    resultArray.append(rightArray[rightPointer])
                    rightPointer += 1
            resultArray.extend(leftArray[leftPointer:])
            resultArray.extend(rightArray[rightPointer:])
            return resultArray
            