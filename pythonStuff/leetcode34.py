from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def leftSearch (nums, target) -> int:
            index = -1
            low, high = 0, len(nums)-1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    index = mid
                    high = mid -1
                elif nums[low] <= target <= nums[mid]:
                    high = mid -1
                else:
                    low = mid + 1
            return index
        def rightSearch (nums, target) -> int:
            index = -1
            low, high = 0, len(nums)-1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    index = mid
                    low = mid +1
                elif nums[mid] <= target <= nums[high]:
                    low = mid +1
                else:
                    high = mid - 1
            return index
        return [leftSearch(nums, target),rightSearch(nums, target)]