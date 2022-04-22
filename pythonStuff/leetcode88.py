class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        leftPointer = 0
        rightPointer = 0
        holder = []
        if len(nums2) == 0:
            return nums1
        else:
            while rightPointer < len(nums2):
                if leftPointer == m:
                    holder.extend(nums2[rightPointer:])
                    for x in range(m+n):
                        nums1[x] = holder[x]  
                    return 
                elif nums1[leftPointer] < nums2[rightPointer]:
                    holder.append(nums1[leftPointer])
                    leftPointer += 1
                else:
                    holder.append(nums2[rightPointer])
                    rightPointer += 1
            
            cleanup = len(nums1)-1
            while leftPointer < cleanup:
                if leftPointer == m:
                    for x in range(m+n):
                        nums1[x] = holder[x]  
                    return
                else:
                    holder.append(nums1[leftPointer])
                    leftPointer += 1
            for x in range(m+n):
                nums1[x] = holder[x]