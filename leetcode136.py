class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ourSet = set()
        for x in nums:
            if not x in ourSet:
                ourSet.add(x)
            else:
                ourSet.remove(x)
        for y in ourSet:
            return y
