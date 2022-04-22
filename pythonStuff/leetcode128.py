class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        highestSeq = 0
        currentSeq = 1
        for x in nums:
            if x-1 in nums:
                continue
            y = x + 1
            while y in nums:
                currentSeq += 1
                y += 1
            if currentSeq > highestSeq:
                highestSeq = currentSeq
            currentSeq = 1
        if currentSeq > highestSeq:
            highestSeq = currentSeq
        return highestSeq