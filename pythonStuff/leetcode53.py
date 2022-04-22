#This solution is called Kadane's algorithm
#Runs in O(n) time

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pointer = 1
        while pointer <= len(nums)-1:
            if nums[pointer-1] > 0:
                nums[pointer] += nums[pointer-1]
            pointer += 1
        return max(nums)