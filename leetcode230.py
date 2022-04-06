# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        
        def getValues(root):
            if root == None:
                return
            values.append(root.val)
            return getValues(root.left), getValues(root.right)
        
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            halfway = len(arr)//2
            leftArr = mergeSort(arr[:halfway])
            rightArr = mergeSort(arr[halfway:])
            leftPointer, rightPointer = 0,0
            result = []
            while leftPointer < len(leftArr) and rightPointer < len(rightArr):
                if leftArr[leftPointer] < rightArr[rightPointer]:
                    result.append(leftArr[leftPointer])
                    leftPointer += 1
                else:
                    result.append(rightArr[rightPointer])
                    rightPointer += 1
            result.extend(leftArr[leftPointer:])
            result.extend(rightArr[rightPointer:])
            return result
        
        getValues(root)
        print(values)
        sortedResult = mergeSort(values)
        print(sortedResult)
        return sortedResult[k-1]
                