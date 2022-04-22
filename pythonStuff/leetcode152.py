class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        numsInvert = nums[::-1]
        for x in range(1,len(nums)):
            nums[x] *= nums[x-1] or 1
            numsInvert[x] *= numsInvert[x-1] or 1
        left = max(nums)
        right = max(numsInvert)
        return max(left, right)
