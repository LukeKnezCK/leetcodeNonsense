class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        holder = []
        while k > len(nums):
            k -= len(nums)
        fromBack = len(nums) - k
        for x in range(fromBack, len(nums)):
            holder.append(nums[x])
        del nums[fromBack:]
        for x in holder[::-1]:
            nums.insert(0, x)