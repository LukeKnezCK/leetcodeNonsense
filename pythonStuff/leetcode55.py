#Initial brute force recursive solution O(n^2)
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         x = 0
#         if len(nums) == 1:
#             return True
#         while nums[x] > 0:
#             if self.canJumpHelper( x+nums[x], nums):
#                 return True
#             else:
#                 nums[x] -= 1
#         return False
            
#     def canJumpHelper(self, x, nums) -> bool:
#         if x >= len(nums)-1:
#             return True
#         while nums[x] > 0:
#             if self.canJumpHelper( x+nums[x], nums):
#                 return True
#             else:
#                 nums[x]-=1
#         return False

#My very epic linear time solution =y
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        jumpCounter = 1
        currentLocation = len(nums)-2
        while currentLocation > 0:
            if nums[currentLocation] >= jumpCounter:
                jumpCounter = 1
                currentLocation -= 1
            else:
                currentLocation -= 1
                jumpCounter += 1
        if nums[currentLocation] >= jumpCounter:
            return True
        else:
            return False