class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        encounteredNums = set()
        for x in nums:
            if x in encounteredNums:
                return True
            else:
                encounteredNums.add(x)
        return False
