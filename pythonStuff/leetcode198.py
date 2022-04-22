class Solution:
    def rob(self, nums: list[int]) -> int:
        leftPointer, rightPointer = 0,0
        for x in nums:
            leftPointer, rightPointer = rightPointer, max(leftPointer+x, rightPointer)
        return rightPointer