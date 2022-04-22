class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for x in range(k):
            highest = float('-inf')
            holder = 0
            for y, num in enumerate(nums):
                if num > highest:
                    highest = num
                    holder = y
            del nums[holder]
        return highest