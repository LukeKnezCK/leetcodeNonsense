class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) < 3:
            if len(nums) == 1:
                return 0
            elif nums[0] > nums[1]:
                return 0
            else:
                return 1
        
        left = 0
        middle = 1
        right = 2
        
        while right < len(nums)-1:
            if nums[middle] > nums[left] and nums[middle] > nums[right]:
                return middle
            left += 1
            middle += 1
            right += 1
        if nums[middle] > nums[left] and nums[middle] > nums[right]:
            return middle
        elif nums[right] > nums[middle]:
            return right
        else:
            return 0