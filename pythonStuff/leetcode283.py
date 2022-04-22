class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        end = len(nums)-1
        x = 0
        while x <= end:
            if nums[x] == 0:
                nums.append(0)
                nums.pop(x)
                end -= 1
            else:
                x += 1
        
