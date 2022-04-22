class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        leftPointer = 0
        rightPointer = 0
        combinedArr = []
        while leftPointer < len(nums1) and rightPointer < len(nums2):
            if nums1[leftPointer] < nums2[rightPointer]:
                combinedArr.append(nums1[leftPointer])
                leftPointer += 1
            else:
                combinedArr.append(nums2[rightPointer])
                rightPointer += 1
        combinedArr.extend(nums1[leftPointer:])
        combinedArr.extend(nums2[rightPointer:])
        if len(combinedArr) % 2 == 0:
            return float((combinedArr[len(combinedArr)//2] + combinedArr[len(combinedArr)//2 -1])/2)
        else:
            return float(combinedArr[len(combinedArr)//2])